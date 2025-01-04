import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class TimePublisher(Node):
    def __init__(self):
        super().__init__('time_publisher')
        self.publisher_ = self.create_publisher(String, 'clock_time', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"Current time: {time.strftime('%H:%M:%S')}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    time_publisher = TimePublisher()
    rclpy.spin(time_publisher)
    time_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
