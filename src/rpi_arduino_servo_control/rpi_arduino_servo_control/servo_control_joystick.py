#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import serial
import time


class ServoControlNode(Node): # MODIFY NAME
    def __init__(self,ser):
        super().__init__("Servo_control_joystick")  

        self.ser_             = ser
        self.servo_timer      = self.create_timer(0.1,self.servo_angle_cmd)      
        
    def servo_angle_cmd(self):
        x_min     = 0
        x_max     = 717
        angle_min = 0
        angle_max = 180

        if self.ser_.in_waiting > 0:
            msg       = self.ser_.readline().decode('utf-8').rstrip()
            # print(msg)
            if msg:
                x         = int(msg)
                print(x)
                angle1    = (x-x_min)*(angle_max-angle_min)/(x_max-x_min)+angle_min   # mapping A0 pin Analog values (0-716) to angle 0-180 deg
                angle     = max(0, min(180, angle1))                                  # clamp if angle1 is out of 0° ≤ angle1 ≤ 180°
                int_cmd   = int(angle)                                                # map function generates float number while Arduino only read int
                cmd       = "servo:" + str(int_cmd) + "\n"
                self.ser_.write(cmd.encode('utf-8'))

        

def main(args=None):

    while True:                                                                         # serial comunication
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
    node = ServoControlNode(ser)  
    rclpy.spin(node)
    ser.close()                          # serial comunication
    rclpy.shutdown()