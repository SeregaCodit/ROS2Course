from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('target_frame', default_value='turtle1'),
        Node(
            package='l13_tf2_listener',
            executable='turtle_tf2_listener',
            name='tf2_listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        )
    ])
