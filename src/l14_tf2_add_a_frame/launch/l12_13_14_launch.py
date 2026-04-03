from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    l13_launch = PathJoinSubstitution([FindPackageShare("l13_tf2_listener"), "launch"])
    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([l13_launch, "l12_l13_launch.py"])
        ),
        Node(
            package="l14_tf2_add_a_frame",
            executable="fixed_frame_tf2_broadcaster",
            name="fixed_broadcaster",
        )
    ])