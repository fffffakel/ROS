import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from action_robot.action import CleaningTask
import math
import time

class TurtleCleaner(Node):
    def __init__(self):
        super().__init__('turtle_cleaner')
        self.action_server = ActionServer(self, CleaningTask, 'cleaning_task', self.handle_task)
        self.cmd = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.x = None
        self.y = None
        self.theta = None
        self.create_subscription(Pose, '/turtle1/pose', self.update_pose, 10)

        self.strip_width = 0.5
        self.speed = 1.0
        self.angle_speed = 1.0
        self.dist_tol = 0.1
        self.angle_tol = 0.1

    def update_pose(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta

    def handle_task(self, goal_handle):
        task = goal_handle.request
        feedback = CleaningTask.Feedback()
        result = CleaningTask.Result()
        distance = 0.0
        points = 0

        while self.x is None:
            rclpy.spin_once(self)
            time.sleep(0.1)

        if task.task_type == 'clean_square':
            distance, points = self.clean_square(task, goal_handle, feedback)
        elif task.task_type == 'return_home':
            distance = self.go_to(task.target_x, task.target_y, goal_handle, feedback)

        result.success = True
        result.total_distance = distance
        result.cleaned_points = points
        goal_handle.succeed()
        self.get_logger().info(f'Готово: {distance:.2f} м, {points} точек')
        return result

    def clean_square(self, task, goal_handle, feedback):
        distance = 0.0
        points = 0

        half_size = task.area_size / 2.0
        left = max(0.5, task.target_x - half_size)
        right = min(10.5, task.target_x + half_size)
        bottom = max(0.5, task.target_y - half_size)
        top = min(10.5, task.target_y + half_size)

        self.get_logger().info(f'Квадрат: центр ({task.target_x:.2f}, {task.target_y:.2f})')

        path = [
            (left, bottom),  
            (right, bottom), 
            (right, top),    
            (left, top),     
            (left, bottom)   
        ]

        for px, py in path:
            distance += self.go_to(px, py, goal_handle, feedback)
            points += 5

        inner_left = left + self.strip_width
        inner_right = right - self.strip_width
        inner_bottom = bottom + self.strip_width
        inner_top = top - self.strip_width

        curr_x = inner_left
        curr_y = inner_bottom
        distance += self.go_to(curr_x, curr_y, goal_handle, feedback)

        direction = 1 
        strips = int((inner_top - inner_bottom) / self.strip_width)

        for i in range(strips + 1):
            target_x = inner_right if direction == 1 else inner_left
            distance += self.go_to(target_x, curr_y, goal_handle, feedback)
            points += int(abs(target_x - curr_x) / 0.1)

            if goal_handle.is_active:
                progress = min(100, int((i + 1) / (strips + 1) * 100))
                feedback.progress_percent = progress
                feedback.current_cleaned_points = points
                feedback.current_x = self.x
                feedback.current_y = self.y
                goal_handle.publish_feedback(feedback)

            if i < strips:
                curr_y += self.strip_width
                distance += self.go_to(target_x, curr_y, goal_handle, feedback)
                points += 5

            direction *= -1
            curr_x = target_x

        return distance, points

    def go_to(self, target_x, target_y, goal_handle=None, feedback=None):
        distance = 0.0
        last_x = self.x
        last_y = self.y

        while math.hypot(target_x - self.x, target_y - self.y) > self.dist_tol:
            if goal_handle and not goal_handle.is_active:
                return distance

            dx = target_x - self.x
            dy = target_y - self.y
            target_angle = math.atan2(dy, dx)
            angle_error = target_angle - self.theta

            while angle_error > math.pi:
                angle_error -= 2 * math.pi
            while angle_error < -math.pi:
                angle_error += 2 * math.pi

            cmd = Twist()
            if abs(angle_error) > self.angle_tol:
                cmd.angular.z = max(-self.angle_speed, min(self.angle_speed, angle_error))
            else:
                cmd.linear.x = min(self.speed, math.hypot(dx, dy))
                cmd.angular.z = 0.0

            self.cmd.publish(cmd)

            if last_x is not None:
                distance += math.hypot(self.x - last_x, self.y - last_y)
            last_x = self.x
            last_y = self.y

            if goal_handle and feedback and goal_handle.is_active:
                feedback.current_x = self.x
                feedback.current_y = self.y
                goal_handle.publish_feedback(feedback)

            rclpy.spin_once(self)
            time.sleep(0.05)

        self.cmd.publish(Twist())
        time.sleep(0.1)
        return distance

def main(args=None):
    rclpy.init(args=args)
    cleaner = TurtleCleaner()
    try:
        rclpy.spin(cleaner)
    except KeyboardInterrupt:
        pass
    cleaner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()