import rclpy
import sys
from rclpy.node import Node
from l4_tutorial_interfaces.srv import AddThreeInts


class AddThreeIntsClient(Node):
    def __init__(self):
        super().__init__('add_three_int_cli')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints_service')

        while not self.cli.wait_for_service(1):
            self.get_logger().info("Waiting for service ...")

        self.req = AddThreeInts.Request()
        self.get_logger().info('Client online')

    
    def send_request(self):
        self.get_logger().info(f'ARGV: {sys.argv}')
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.req.c = int(sys.argv[3])
        self.future = self.cli.call_async(self.req)
        self.get_logger().info(f"future: {self.future}")


    @property
    def future(self):
        return self._future
    

    @future.setter
    def future(self, value):
        self._future = value


def main():
    rclpy.init()
    node = AddThreeIntsClient()
    node.send_request()

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().info(f'Service call failed: {e}')
            else:
                node.get_logger().info(f'result for add three ints: for {node.req.a} + {node.req.b} + {node.req.c} = {response.sum}')
            break
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()