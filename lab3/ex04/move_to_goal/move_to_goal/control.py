from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node
import rclpy
import sys
import math
import time

class TurtleBot(Node):

	def __init__(self):
		super().__init__('move_to_goal')
		self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.update_pose,10)
		
		self.pose = Pose()
		 
		self.goal_x = float(sys.argv[1])
		self.goal_y = float(sys.argv[2])
		self.goal_theta = float(sys.argv[3]) * math.pi / 180 # в радианах
		self.flag = True
		self.timer = self.create_timer(0.5,self.activate)		
		
	def update_pose(self, data):
		self.pose = data
		
	def activate(self):
		msg = Twist()
		
		self.get_logger().info(f'координаты начала {self.pose}')
		dist = math.sqrt(abs(self.pose.x - self.goal_x)**2 + abs(self.pose.y - self.goal_y))
		

		angle_to_dist = math.atan2(self.goal_y - self.pose.y, self.goal_x - self.pose.x) - self.pose.theta

		self.get_logger().info(f'надо проехать {dist} метров и под углом {angle_to_dist *180 / math.pi} градусов ') 
		# поворот на нужный угол
		
		msg.angular.z = angle_to_dist
		self.publisher.publish(msg)
		time.sleep(1)
		self.get_logger().info('поворот выполнен')
		msg.angular.z = 0.0
		msg.linear.x = dist
		self.publisher.publish(msg)
		time.sleep(1)
		self.get_logger().info('движение завершено')
		self.timer.destroy()
		self.timer = self.create_timer(0.1,self.final_rotate)
		return
	def final_rotate(self):
		msg = Twist()
		self.get_logger().info(f'координаты {self.pose.theta} {self.goal_theta}')
		
		if abs(self.pose.theta - self.goal_theta) <= math.pi/12:
			self.timer.destroy()
			sys.exit(0)

		msg.angular.z = math.pi/32
		self.publisher.publish(msg)
		time.sleep(1)
	def normalize_angle(self, angle):
			
		return math.atan2(math.sin(angle), math.cos(angle))



def main(args=None):
	rclpy.init(args=args)
	x = TurtleBot()
	rclpy.spin(x)
	x.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()