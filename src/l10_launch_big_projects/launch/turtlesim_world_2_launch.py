from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            # namespace='turtlesim2',  визначаємо namespace через GroupActions(PushROSNamespace) в головному лаунч файлі
            name='sim',
            parameters=[
                PathJoinSubstitution([
                    FindPackageShare('l10_launch_big_projects'), 'config', 'turtlesim.yaml'
                ]),
            ]
        ),
    ])