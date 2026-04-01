import rclpy
from rclpy.node import Node

from l4_tutorial_interfaces.msg import Num

class NumPublisher(Node):
    def __init__(self):
        super().__init__('num_publisher')
        self.pub = self.create_publisher(Num, 'num_pub', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self._timer_callback)
        self.i = 0

    
    def _timer_callback(self):
        msg = Num()
        msg.num = self.i
        self.pub.publish(msg)
        self.get_logger().info(f'publishing: {msg}')
        self.i += 1


def main():
    rclpy.init()
    node = NumPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
