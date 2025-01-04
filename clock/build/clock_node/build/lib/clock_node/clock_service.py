import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

import datetime


class ClockServiceNode(Node):
    def __init__(self):
        super().__init__("clock_service")
        self.service = self.create_service(Trigger, "get_time", self.callback)
        self.get_logger().info("Clock Service is ready to provide the time.")

    def callback(self, request, response):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response.success = True
        response.message = f"Current time is: {current_time}"
        self.get_logger().info(f"Provided time: {current_time}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ClockServiceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()


if __name__ == "__main__":
    main()
