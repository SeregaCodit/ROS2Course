from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='l5_parameters',
            executable='some_parameter_node',
            name='custom_parameter_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {
                    'some_parameter': 'earth'
                }
            ]
        )
    ])