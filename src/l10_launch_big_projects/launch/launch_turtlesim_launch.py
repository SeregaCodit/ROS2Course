from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import PushROSNamespace
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    a = 2
    b =3
    c = a + b
    launch_dir = PathJoinSubstitution([FindPackageShare('l10_launch_big_projects'), 'launch'])

    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'turtlesim_world_1_launch.py'])
        ),
        GroupAction(
            actions=[
                PushROSNamespace('turtlesim2'),
                IncludeLaunchDescription(
                    PathJoinSubstitution([launch_dir, 'turtlesim_world_2_launch.py'])
                )
            ]
        ),

        # IncludeLaunchDescription(
        #     PathJoinSubstitution([launch_dir, 'turtlesim_world_2_launch.py'])
        # ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'turtlesim_world_3_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'broadcaster_listener_launch.py']),
            launch_arguments={'target_frame': 'carrot1'}.items()
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'mimic_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'fixed_broadcaster_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'turtlesim_rviz_launch.py'])
        )
    ])