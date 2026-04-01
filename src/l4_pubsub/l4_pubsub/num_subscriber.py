import rclpy
from rclpy.node import Node

from l4_tutorial_interfaces.msg import Num


class NumSubscriber(Node):
    def __init__(self):
        super().__init__('num_subscriber')
        self.sub = self.create_subscription(Num, 'num_pub', self._listener_callback, 10)
        self.sub

    def _listener_callback(self, msg):
        self.get_logger().info(f'I heard {msg.num}')


def main():
    rclpy.init()
    node = NumSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()