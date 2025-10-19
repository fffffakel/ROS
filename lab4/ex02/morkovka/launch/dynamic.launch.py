import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    
    # Launch arguments
    radius_arg = DeclareLaunchArgument(
        'radius',
        default_value='2.0',
        description='Distance from turtle1 to carrot'
    )
    
    direction_arg = DeclareLaunchArgument(
        'direction_of_rotation',
        default_value='1',
        description='Rotation direction: 1 for clockwise, -1 for counterclockwise'
    )
    
    target_frame_arg = DeclareLaunchArgument(
        'target_frame',
        default_value='carrot1',
        description='Target frame for turtle2 to follow'
    )

    # Nodes
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='sim'
    )
    
    broadcaster1_node = Node(
        package='morkovka',
        executable='turtle_tf2_broadcaster',
        name='broadcaster1',
        parameters=[{'turtlename': 'turtle1'}]
    )
    
    broadcaster2_node = Node(
        package='morkovka',
        executable='turtle_tf2_broadcaster',
        name='broadcaster2',
        parameters=[{'turtlename': 'turtle2'}]
    )
    
    listener_node = Node(
        package='morkovka',
        executable='turtle_tf2_listener',
        name='listener',
        parameters=[{'target_frame': LaunchConfiguration('target_frame')}]
    )
    
    carrot_broadcaster_node = Node(
        package='morkovka',
        executable='dynamic_frame_tf2_broadcaster',
        name='carrot_broadcaster',
        parameters=[
            {'radius': LaunchConfiguration('radius')},
            {'direction_of_rotation': LaunchConfiguration('direction_of_rotation')}
        ]
    )

    return LaunchDescription([
        radius_arg,
        direction_arg,
        target_frame_arg,
        turtlesim_node,
        broadcaster1_node,
        broadcaster2_node,
        listener_node,
        carrot_broadcaster_node,
    ])