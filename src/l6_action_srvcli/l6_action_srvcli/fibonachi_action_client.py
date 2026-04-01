import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.task import Future

import sys

from l6_actions.action import Fibonachi


class FibonachiActionClient(Node):
    def __init__(self):
        super().__init__('fibonachi_action_client')
        self._action_client = ActionClient(
            self,
            Fibonachi,
            'calc_fibonachi'
        )

    
    def send_goal(self, order: int):
        self.get_logger().info(f'Got order: {order}')
        goal_msg = Fibonachi.Goal()
        goal_msg.order = order

        self.get_logger().info("Waiting for server...")
        self._action_client.wait_for_server()
        self.get_logger().info('Server is available!')

        self._send_goal_future = self._action_client.send_goal_async(goal_msg, self.feefback_callback)
        self.get_logger().info('sending goal msg to server...')

        self._send_goal_future.add_done_callback(self._goal_response_callback)
    

    def _goal_response_callback(self, future: Future):
        self.get_logger().info(f'Got future: {future}')
        goal_handle = future.result()
        self.get_logger().info(f"Got goal_handle: {goal_handle}")
        if not goal_handle.accepted:
            self.get_logger().warning('Goal rejected :(')

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self._get_result_callback)


    def _get_result_callback(self, future: Future):
        result = future.result().result
        self.get_logger().info(f'Result: {result.sequence}')
        rclpy.shutdown()


    def feefback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Recived feedback: {feedback.partial_sequence}')

def main():
    rclpy.init()
    action_client = FibonachiActionClient()

    action_client.send_goal(int(sys.argv[1]))
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()