#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from robot_interfaces.srv import CreateFolder

import os
HOME  =  os.path.expanduser('~')

class CreateFolderNode(Node):
    def __init__(self):
        super().__init__("create_desired_folder_server")  # instructor . node name in "ros2 node list"
        self.create_folder_server = self.create_service(CreateFolder,"shayan_create_folder",self.create_folder_callback) # service name in "Ros2 service list"

        self.get_logger().info("Shayan node of create folder has been started")

    def create_folder_callback(self,request,response):
        folder_name = request.folder_name
        
        try:
            os.makedirs(HOME+"/"+folder_name, exist_ok=True)
            response.success = True
        except FileExistsError:
            response.success = False
            response.message = "Folder already exists"
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response



def main(args=None):
    rclpy.init(args=args)
    node = CreateFolderNode()
    rclpy.spin(node)
    rclpy.shutdown()