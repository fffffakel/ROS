from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Первый turtlesim узел (ведущая черепаха)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim1',
            output='screen'
        ),
        
        # Второй turtlesim узел (первая следующая черепаха)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim2',
            output='screen'
        ),
        
        # Третий turtlesim узел (вторая следующая черепаха)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim3',
            output='screen'
        ),
        
        # Узел mimic для второй черепахи (следует за первой)
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            parameters=[{'input_topic': '/turtle1/cmd_vel', 'output_topic': '/turtle2/cmd_vel'}]
        ),
        
        # Узел mimic для третьей черепахи (следует за второй)
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            parameters=[{'input_topic': '/turtle2/cmd_vel', 'output_topic': '/turtle3/cmd_vel'}]
        )
    ])