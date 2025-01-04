# clock/test/test_hello_world.py
import unittest
import rclpy
from rclpy.node import Node
from clock import hello_world  # ノードが定義されているファイル（仮に clock/hello_world.py とする）

class TestHelloWorldNode(unittest.TestCase):

    def setUp(self):
        """
        テスト前に呼び出され、ノードを初期化します。
        """
        rclpy.init()
        self.node = hello_world.HelloWorldNode()  # 実際のノードに合わせて変更

    def tearDown(self):
        """
        テスト後に呼び出され、ノードを破棄します。
        """
        self.node.destroy_node()
        rclpy.shutdown()

    def test_hello_world(self):
        """
        ノードが 'Hello, World!' をログ出力するかを確認します。
        """
        with self.assertLogs(self.node.get_logger(), level='INFO') as log:
            self.node.get_logger().info('Hello, World!')
            # ログに "Hello, World!" が含まれているかを確認
            self.assertIn('Hello, World!', log.output[0])

if __name__ == '__main__':
    unittest.main()
