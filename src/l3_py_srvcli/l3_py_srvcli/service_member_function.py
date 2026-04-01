import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class MinimalServiceNode(Node):
    def __init__(self):
        super().__init__('minimal_service')

        self.srv = self.create_service(AddTwoInts, 'add_two_ints_srv', self._add_two_callback)
        self.get_logger().info("service started!")

    
    def _add_two_callback(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming request:\na={request.a} b={request.b}")
        return response


def main():
    rclpy.init()
    minimal_service = MinimalServiceNode()
    rclpy.spin(minimal_service)

    # node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()