import sys
import time
from sensor_interfaces.srv import RequestSensorData
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LoadCellClient(Node):
    def __init__(self):
        super().__init__('load_cell_client')
        self.client = self.create_client(RequestSensorData, 'get_load_cell_data')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request = RequestSensorData.Request()
        self.publisher1 = self.create_publisher(String, 'load_cell1_data', 10)
        self.publisher2 = self.create_publisher(String, 'load_cell2_data', 10)

    def send_request(self, id):
        self.request.id = id
        return self.client.call_async(self.request)

    def publish_load_cell_data(self, data, id):
        msg = String()
        msg.data = data
        if id==1:
            self.publisher1.publish(msg)
        elif id==2:
            self.publisher2.publish(msg)

def main():
    rclpy.init()
    load_cell_client = LoadCellClient()
    publish_rate = 500 #Hz
    while rclpy.ok():
        # Request data for load cell 1 and publish
        future = load_cell_client.send_request(1)
        rclpy.spin_until_future_complete(load_cell_client, future)
        response = future.result()
        load_cell_client.publish_load_cell_data(response.data, 1)
        
        # Request data for load cell 2 and publish
        future = load_cell_client.send_request(2)
        rclpy.spin_until_future_complete(load_cell_client, future)
        response = future.result()
        load_cell_client.publish_load_cell_data(response.data, 2)

        # Sleep to achieve desired publish rate
        time.sleep(1.0/publish_rate)

    load_cell_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()