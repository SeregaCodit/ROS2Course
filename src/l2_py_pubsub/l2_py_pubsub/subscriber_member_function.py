import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriberNode(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')

        self.sub = self.create_subscription(
            String,
            'topic',
            self._listener_callback,
            10
        )

        self.sub # prevent unused variable warning
    

    def _listener_callback(self, msg: String):
        self.get_logger().info(f"I heard {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber_node = MinimalSubscriberNode()

    rclpy.spin(minimal_subscriber_node)

    minimal_subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()