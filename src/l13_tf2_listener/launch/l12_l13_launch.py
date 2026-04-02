from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration

from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    l12_pkg_launch = PathJoinSubstitution([FindPackageShare('l12_tf2_broadcaters'), 'launch'])
    l13_pkg_launch = PathJoinSubstitution([FindPackageShare('l13_tf2_listener'), 'launch'])
    return LaunchDescription([
        DeclareLaunchArgument(
            'target_frame',
            default_value='turtle1',
            description='The name of target frame'
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([l12_pkg_launch, 'l12_tf2_broadcaster_launch.py'])
            ),
        IncludeLaunchDescription(
            PathJoinSubstitution([l13_pkg_launch, 'l13_launch.py']),
            launch_arguments={'target_farme': LaunchConfiguration('target_frame')}.items()
        )
    ])