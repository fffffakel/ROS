import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class DynamicFrameBroadcaster(Node):

    def __init__(self):
        super().__init__('dynamic_frame_tf2_broadcaster')
        
        self.declare_parameter('radius', 2.0)
        self.declare_parameter('direction_of_rotation', 1)
        
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)
        
        self.get_logger().info("Carrot TF2 broadcaster started!")

    def broadcast_timer_callback(self):

        radius = self.get_parameter('radius').value
        direction = self.get_parameter('direction_of_rotation').value
        
        seconds = self.get_clock().now().nanoseconds / 1e9

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot1'
        
        angle = seconds * direction  
        t.transform.translation.x = float(math.cos(angle) * radius)
        t.transform.translation.y = float(math.sin(angle) * radius)
        t.transform.translation.z = 0.0
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self.tf_broadcaster.sendTransform(t)


def main():
    rclpy.init()
    node = DynamicFrameBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()