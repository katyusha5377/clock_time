import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TimeSubscriber(Node):
    def __init__(self):
        super().__init__('time_subscriber')
        self.subscription = self.create_subscription(
            String,
            'clock_time',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    time_subscriber = TimeSubscriber()
    rclpy.spin(time_subscriber)
    time_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
