#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import sys
import tty
import termios
# from std_msgs.msg import String
from std_msgs.msg import Int32
import threading

# class Read_key(Node):
#     def __init__(self):
#         super().__init__("read_key")
#         self.read_key_pub = self.create_publisher(String,"key",10)
#         self.timer = self.create_timer(1,self.send_key_reading())

#     def send_key_reading(self):
#         msg = String()
#         key = sys.stdin.read(1)
#         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
#         msg.data = key
#         self.get_logger().info(f"key read {msg.data}")
#         self.read_key_pub.publish(msg)


def getKey(settings):
    tty.setraw(sys.stdin.fileno())
    # sys.stdin.read() returns a string on Linux
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def restoreTerminalSettings(old_settings):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def main(args=None):
    settings = termios.tcgetattr(sys.stdin)
    rclpy.init()
    node = rclpy.create_node("read_key_stroke")

    # msg = String()
    msg = Int32()

    pub = node.create_publisher(Int32, 'key', 10)

    spinner = threading.Thread(target=rclpy.spin, args=(node,))
    spinner.start()

    while True:
        key = getKey(settings)
        if (key == '\x03'):
            break
        if (key not in ['w','a','s','d','b']):
            continue
        if key == "w":
            msg.data=1
        if key == "a":
            msg.data=2
        if key == "s":
            msg.data=3
        if key == "d":
            msg.data=4
        if key == "b":
            msg.data=0

        # msg.data = key
        pub.publish(msg)

    rclpy.shutdown()
    spinner.join()
    restoreTerminalSettings(settings)


if __name__ == '__main__':
    main()