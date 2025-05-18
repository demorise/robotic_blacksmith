import sys
from sensor_interfaces.srv import RequestSensorData
import rclpy
from rclpy.node import Node

class LoadCellClient(Node):

    def __init__(self):
        super().__init__('load_cell_client')
        self.client = self.create_client(RequestSensorData, 'get_load_cell_data')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request = RequestSensorData.Request()

    def send_request(self, id):
        self.request.id = id
        return self.client.call_async(self.request)

    def publish_load_cell_data(data, publisher):
        pass

def main():
    rclpy.init()
    load_cell_client = LoadCellClient()

    future = load_cell_client.send_request(1)
    rclpy.spin_until_future_complete(load_cell_client, future)
    response = future.result()
    load_cell_client.get_logger().info(
        'Data from load cell %i is = %s' % (1, response.data))

    load_cell_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()