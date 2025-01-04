# 必要なパッケージを探します
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_gtest REQUIRED)

# 他のパッケージの検索も行う
find_package(rclpy REQUIRED)

ament_add_gtest(test_hello_world
  test/test_hello_world.py
)
