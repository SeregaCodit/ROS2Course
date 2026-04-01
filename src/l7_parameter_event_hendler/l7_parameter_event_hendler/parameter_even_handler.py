import rclpy
from rclpy.node import Node
import rclpy.parameter
from rclpy.parameter_event_handler import ParameterEventHandler


class NodeWithParameters(Node):
    def __init__(self):
        super().__init__('node_with_parameters')

        self.declare_parameter('int_param_1', 0)
        self.declare_parameter('double_param_1', 0.0)

        self.handler = ParameterEventHandler(self)

        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name='param_1',
            node_name='node_with_parameters',
            callback=self._callback
        )

        self.callback_handle_2 = self.handler.add_parameter_callback(
            parameter_name='a_double_param',
            node_name='parameter_blackboard',
            callback=self._callback
        )

        self.event_callback_param = self.handler.add_parameter_event_callback(
            callback=self._event_callback
        )

        self.get_logger().info(f'{self.get_name()} node created!')
    
    def _callback(self, param: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(f'Recived an update to parameter: {param.name} - {rclpy.parameter.parameter_value_to_python(param.value)}')


    def _event_callback(self, param_event):
        self.get_logger().info(f"Recived param event from node: {param_event.node}")

        for param in param_event.changed_parameters:
            self.get_logger().info(
                f'Inside event: {param.name} changed to {rclpy.parameter.parameter_value_to_python(param.value)}'
            )


def main():
    rclpy.init()
    node_with_params = NodeWithParameters()
    rclpy.spin(node_with_params)

    node_with_params.destroy_node()
    rclpy.shutdown()