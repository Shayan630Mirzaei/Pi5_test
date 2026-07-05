#!/usr/bin/env python3

import serial
import time

last_time_vmd_send = time.time()


#Initi serial
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

try:

    while True:
        time.sleep(0.01)
        if ser.in_waiting > 0: 
            msg = ser.readline().decode('utf-8').rstrip()
            print (msg)
 
        time_now = time.time()

        if time_now - last_time_vmd_send>1.0:
            last_time_vmd_send = time_now
            ser.write("test'\n".encode('utf-8'))

except KeyboardInterrupt:
    print ("Closing Serial Comunincation")
    ser.close()




