#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 


class Subscriber(Node) : 
    def __init__(self) : 
        super().__init__("Gui")
        self.control_sginal_subscriber=self.create_subscription(String,'feedback',self.control_signal_callback,10)
        # self.shape_data_subscriber=self.create_subscription(String,'detected_shapes',self.shape_data_callback,10)
        # self.get_logger().info('Shape Subscriber has been started ')

    def control_signal_callback(self,msg) : 
        self.get_logger().info(f'Received control signal : {msg.data}')

    def shape_data_callback(self,msg) : 
        self.get_logger().info(f'Received Detected shapes : {msg.data}')

def main(args=None) : 
    rclpy.init(args=args)
    node=Subscriber()
    rclpy.spin(node)
    # Subscriber_.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__' : 
    main()
