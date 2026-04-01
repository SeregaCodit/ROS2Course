import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter


class ParamNode(Node):
    def __init__ (self):
        super().__init__('some_parameter_node')
        
        from rcl_interfaces.msg import ParameterDescriptor
        
        some_param_descriptor = ParameterDescriptor(decription='Some description for some_parameter')

        self.declare_parameter('some_parameter', 'world', some_param_descriptor) # тип параметру визначається автоматично із значення за замовчуванням
        self.timer = self.create_timer(1, self._timer_callback)

    
    def _timer_callback(self):
        some_param = self.get_parameter('some_parameter').get_parameter_value().string_value  # отримуємо параметр
        self.get_logger().info(f'Hello, {some_param}!')

        # повертає параметр до значення за замовчуванням - 'word'
        some_new_param = Parameter(
            'some_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )

        all_new_params = [some_new_param]
        self.set_parameters(all_new_params)


def main():
    rclpy.init()
    param_node = ParamNode()

    rclpy.spin(param_node)

    param_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
