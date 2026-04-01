import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        self.pub = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self._timer_callback)
        self.i = 1

    
    def _timer_callback(self):
        msg = String()
        msg.data = f"Hello Word {self.i}"
        self.pub.publish(msg=msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    minimall_publisher_node = MinimalPublisher()
    rclpy.spin(minimall_publisher_node)

    minimall_publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

