import socket
import sys
import numpy as np
import time
from sensor_interfaces.srv import RequestSensorData
import rclpy
from rclpy.node import Node

class LoadCellService(Node):
    def __init__(self):
        super().__init__('load_cell_server')
        self.srv = self.create_service(RequestSensorData, 'get_load_cell_data', self.sensor_data_callback)
        self.NUMBER_OF_SAMPLES = 10

        # Connect the socket to first sensor
        self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.3', 10000)
        print('connecting to {} port {}'.format(*server_address))
        self.sock1.connect(server_address)

        # Connect the socket to sensor sensor
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.5', 10000)
        print('connecting to {} port {}'.format(*server_address))
        self.sock2.connect(server_address)

    def sensor_data_callback(self, request, response):
        # self.get_logger().info('Received request for load cell with id %i'% request.id)
        message_string = str(self.NUMBER_OF_SAMPLES)
        message = message_string.encode()
        
        if (request.id==1):
            self.sock1.sendall(message)
            byte_data = self.sock1.recv(10000)
            data =  np.frombuffer(byte_data)
            response.data = np.array_str(data)
        elif (request.id==2):
            self.sock2.sendall(message)
            byte_data = self.sock2.recv(10000)
            data =  np.frombuffer(byte_data)
            response.data = np.array_str(data)
        # print(response.data)  
        return response

    def __del__(self):
        print('Closing socket connections')
        self.sock1.close()
        self.sock2.close()

def main():
    rclpy.init()
    load_cell_server = LoadCellService()
    rclpy.spin(load_cell_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()