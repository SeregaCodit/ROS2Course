import rclpy
import sys

from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MinimalClientAsyncNode(Node):
    def __init__(self):
        super().__init__('minimal_client_async')

        self.cli = self.create_client(AddTwoInts, 'add_two_ints_srv')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('minimal_client is waiting for add_two_ints_srv service')

        self.request = AddTwoInts.Request()

    def send_request(self, a: int, b: int):
        self.request.a = a
        self.request.b = b
        return self.cli.call_async(self.request)
    

def main():
    rclpy.init()
    node = MinimalClientAsyncNode()

    future = node.send_request(a=int(sys.argv[1]), b=int(sys.argv[2]))
    rclpy.spin_until_future_complete(node=node, future=future)
    response = future.result()
    node.get_logger().info(f"Result of add_two_ints_srv: for {int(sys.argv[1])} + {int(sys.argv[2])} = {response.sum}")
    
    node.destroy_node()
    rclpy.shutdown()


    if __name__ == "__main__":
        main()
            