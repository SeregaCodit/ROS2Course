from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('turtlename', default_value='turtle1'),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='l12_tf2_broadcaters',
            executable='turtle_tf2_broadcaster',
            name='broadcaster_pose',
            parameters=[
                {'turtlename': LaunchConfiguration('turtlename')}
            ]
        ),
    ])