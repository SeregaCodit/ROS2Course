from launch import LaunchDescription
from launch_ros.actions import Node

PACKAGE = 'l2_py_pubsub'

def generate_launch_description():
    return LaunchDescription([
        Node(
            package=PACKAGE,
            executable='talker',
            name='talker_name'
        ),
        Node(
            package=PACKAGE,
            executable="listener",
            name="listener_name"
        )
    ])