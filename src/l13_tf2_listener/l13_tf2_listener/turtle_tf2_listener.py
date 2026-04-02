import math

from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node
import rclpy.time

from tf2_ros import TransformException # type: ignore
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from turtlesim.srv import Spawn


class FrameListener(Node):
    def __init__(self):
        super().__init__('turtle_tf2_frame_listener')

        #declare and acquire 'trget_frame' parameter
        self.target_frame = self.declare_parameter(
            'target_frame', 'turtle1'
        ).get_parameter_value().string_value

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # create a client spawn turtle
        self.spawner = self.create_client(Spawn, 'spawn')
        # bool vals to store the information
        # if the service for spawnitg turtle is available
        self.turtle_spawn_service_ready = False
        # if the turtle was spawned successfully
        self.turtle_spawned = False

        # create turtle2 velocity publisher
        self.publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 1)

        # call on_timer func every second
        self.timer = self.create_timer(1.0, self.on_timer)


    def on_timer(self):
        """
        Store frame names in variables that will be used to
        compute transformations
        """

        from_frame_rel = self.target_frame
        to_frame_rel = 'turtle2'

        if self.turtle_spawn_service_ready:
            if self.turtle_spawned:
                # look uo for the transformation between from_frame_rel and to_frame_rel frames
                # and send velocity commands for 'to_frame_rel' to reach to_frame_rel
                try:
                    t = self.tf_buffer.lookup_transform(
                        to_frame_rel,
                        from_frame_rel,
                        rclpy.time.Time()
                    )
                except TransformException as ex:
                    self.get_logger().info(
                        f'Could not transorm {from_frame_rel} to {to_frame_rel}: {ex}'
                    )
                    return
                
                msg = Twist()
                scale_rotation_rate = 1.0
                msg.angular.z = scale_rotation_rate * math.atan2(
                    t.transform.translation.y,
                    t.transform.translation.x
                )

                scale_forward_speed = 0.5
                msg.linear.x = scale_forward_speed * math.sqrt(
                    t.transform.translation.x ** 2 +
                    t.transform.translation.y ** 2
                )

                self.publisher.publish(msg)
            
            else:
                if self.result.done():
                    self.get_logger().info(
                        f'Successfully spawned {self.result.result().name}'  # type: ignore
                    )
                    self.turtle_spawned = True
                else:
                    self.get_logger().info('Spawn is not finished')
        else:
            if self.spawner.service_is_ready():
                # initialize request with turtle name and coordinates
                # x, y and theta are defined as floats in turtlesim/srv/Spawn
                request = Spawn.Request()
                request.name = 'turtle2'
                request.x = float(4)
                request.y = float(2)
                request.theta = float(0)
                # call request
                self.result = self.spawner.call_async(request)
                self.turtle_spawn_service_ready = True
            else:
                self.get_logger().info('Service is not ready')


def main():
    rclpy.init()
    node = FrameListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()