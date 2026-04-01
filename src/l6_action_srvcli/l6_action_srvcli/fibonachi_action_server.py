import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from l6_actions.action import Fibonachi
from rclpy.action.server import ServerGoalHandle
import time


class FibonachiActionServer(Node):
    def __init__(self):
        super().__init__('fibonachi_action_server')

        self._action_server = ActionServer(
            self,
            Fibonachi,
            'calc_fibonachi',
            self._execute_callback
        )
        self.get_logger().info('fibonachi server created!')


    def _execute_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info(f'Executing goal {goal_handle.request}...')
        order = goal_handle.request.order
        
        feedback_msg = Fibonachi.Feedback()
        feedback_msg.partial_sequence = [0, 1]
        
        # feedback sending
        for i in range(1, order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i - 1]
            )

            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()
        result = Fibonachi.Result()
        result.sequence = feedback_msg.partial_sequence
        return result
    

def main():
    rclpy.init()
    fibonachi_action_server = FibonachiActionServer()
    rclpy.spin(fibonachi_action_server)

    fibonachi_action_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()