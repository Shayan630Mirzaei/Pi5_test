#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import serial
import time


class ArduinoDriverNode(Node): # MODIFY NAME
    def __init__(self,ser):
        super().__init__("LED_blink_driver") # MODIFY NAME
        
        self.ser_             = ser
        self.led_on_          = False
        self.led_blink_timer_ = self.create_timer(1.0,self.blink_led)

    def blink_led(self):
        cmd          = "led:"+str(int(self.led_on_))+"\n"
        self.ser_.write(cmd.encode('utf-8'))
        self.led_on_ = not self.led_on_       



def main(args=None):
    while True:
        try:
            ser = serial.Serial('/dev/ttyACM0',115200,timeout=1.0)
            print("Successfully connected to serial.")
            time.sleep(1)
            ser.reset_input_buffer()
            break

        except serial.SerialException:
            print("Couldn't connect to Serial. Retrying in 1 second...")
            time.sleep(1)


    rclpy.init(args=args)
    node = ArduinoDriverNode(ser) # MODIFY NAME
    rclpy.spin(node)
    ser.close()
    rclpy.shutdown()