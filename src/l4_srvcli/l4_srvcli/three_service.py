import rclpy
from rclpy.node import Node
from l4_tutorial_interfaces.srv import AddThreeInts

class AddThreeIntsService(Node):
    def __init__(self):
        super().__init__('add_three_ints_srv')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints_service', self._add_three_ints_callback)
        self.get_logger().info("Service online")

    
    def _add_three_ints_callback(self, req, res):
        res.sum = req.a + req.b + req.c
        self.get_logger().info(f'Got request: a = {req.a} b = {req.b} c = {req.c}')
        return res
    

def main():
    rclpy.init()
    node = AddThreeIntsService()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()