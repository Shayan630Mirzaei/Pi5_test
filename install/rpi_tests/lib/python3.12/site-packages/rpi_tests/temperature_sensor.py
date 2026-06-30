#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from gpiozero import CPUTemperature
from example_interfaces.msg import Float64


class TempSensNode(Node):
    def __init__(self):
        super().__init__("temperature_sensor")
        self.get_logger().info("Temperature sensor node has been started")
        
        self.temperature_pub_   = self.create_publisher(Float64,"RPI5_temp",10)
        self.temperature_timer_ = self.create_timer(1.0,self.temp_callback)

        # self.get_logger().info(f"CPU temperature is: {CPUTemperature().temperature:.1f} deg C")

    def temp_callback(self):
        msg      = Float64()
        msg.data = CPUTemperature().temperature
        self.temperature_pub_.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    node = TempSensNode()
    rclpy.spin(node)
    rclpy.shutdown()

