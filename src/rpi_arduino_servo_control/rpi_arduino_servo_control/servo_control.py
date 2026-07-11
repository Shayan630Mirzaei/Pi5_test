#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import serial
import time


class ServoControlNode(Node): # MODIFY NAME
    def __init__(self,ser):
        super().__init__("Servo_control")  

        self.ser_             = ser
        self.index            = 0
        self.going_up         = True
        self.servo_timer      = self.create_timer(0.1,self.servo_sweep)                                                    # serial comunication


# servo:000
    def servo_sweep(self):
    #    print(self.index)
       cmd  = "servo:" + str(self.index) + "\n"
       self.ser_.write(cmd.encode('utf-8'))

       if self.going_up:
            if self.index>=180:
                self.going_up = False
            else:
                self.index   +=1
       else:
            if self.index <= 0:
                self.going_up = True
            else:
                self.index   -=1

        









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