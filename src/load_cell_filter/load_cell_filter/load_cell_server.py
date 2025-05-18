from sensor_interfaces.srv import RequestSensorData
import rclpy
from rclpy.node import Node

class LoadCellService(Node):
    def __init__(self):
        super().__init__('load_cell_server')
        self.srv = self.create_service(RequestSensorData, 'get_load_cell_data', self.sensor_data_callback)

    def sensor_data_callback(self, request, response):
        response.data = 'test_data'
        self.get_logger().info('Received request for load cell with id %i'% request.id)
        return response

def main():
    rclpy.init()

    load_cell_server = LoadCellService()

    rclpy.spin(load_cell_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()