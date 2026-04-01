from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('x', default_value='0'),
        DeclareLaunchArgument('y', default_value='0'),
        DeclareLaunchArgument('z', default_value='1'),
        DeclareLaunchArgument('yaw', default_value='0'),
        DeclareLaunchArgument('pitch', default_value='0'),
        DeclareLaunchArgument('roll', default_value='0'),
        DeclareLaunchArgument('frame_id', default_value='world'),
        DeclareLaunchArgument('child_frame_id', default_value='mystaticturtle'),

        
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_static_link',
            arguments = [
                '--x', LaunchConfiguration('x'), '--y', LaunchConfiguration('y'), '--z', LaunchConfiguration('z'),
                '--yaw', LaunchConfiguration('yaw'), '--pitch', LaunchConfiguration('pitch'), '--roll', LaunchConfiguration('roll'),
                '--frame-id', LaunchConfiguration('frame_id'), '--child-frame-id', LaunchConfiguration('child_frame_id')
            ],
        ),
    ])