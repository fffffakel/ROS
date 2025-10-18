import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from action_robot.action import CleaningTask

class TurtleClient(Node):
    def __init__(self):
        super().__init__('turtle_client')
        self.client = ActionClient(self, CleaningTask, 'cleaning_task')
        self.results = []

    def send_task(self, task_type, size, x, y):
        goal = CleaningTask.Goal()
        goal.task_type = task_type
        goal.area_size = size
        goal.target_x = x
        goal.target_y = y

        self.get_logger().info(f'Задача: {task_type}, размер {size}')
        self.client.wait_for_server()

        future = self.client.send_goal_async(goal, feedback_callback=self.show_progress)
        rclpy.spin_until_future_complete(self, future)

        if not future.result() or not future.result().accepted:
            self.get_logger().info('Задача отклонена')
            return

        self.get_logger().info('Задача принята')
        result_future = future.result().get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        if result_future.result():
            result = result_future.result().result
            self.results.append(result)
            self.get_logger().info(
                f'Готово: успех={result.success}, '
                f'точек={result.cleaned_points}, '
                f'пройдено={result.total_distance:.2f}')

    def show_progress(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            f'Прогресс: {feedback.progress_percent}% | '
            f'Точек: {feedback.current_cleaned_points} | '
            f'({feedback.current_x:.2f}, {feedback.current_y:.2f})')

def main():
    rclpy.init()
    client = TurtleClient()

    tasks = [
        ('clean_square', 4.0, 5.0, 5.0),
        ('return_home', 0.0, 1.0, 1.0),
    ]

    for task in tasks:
        client.send_task(*task)

    client.get_logger().info('=== УБОРКА ЗАВЕРШЕНА ===')
    total_points = sum(r.cleaned_points for r in client.results)
    total_distance = sum(r.total_distance for r in client.results)
    client.get_logger().info(f'Всего точек: {total_points}')
    client.get_logger().info(f'Всего пройдено: {total_distance:.2f}')

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()