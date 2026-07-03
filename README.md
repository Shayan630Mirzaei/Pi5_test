# Raspberry Pi ↔ Arduino Serial Communication Demo

A minimal example demonstrating bidirectional serial communication between a Raspberry Pi (Python) and an Arduino board (C++), using a non-blocking, timer-based loop on both ends.

## What it does

- The **Pi** connects to the Arduino over USB serial, sends the message `test` every 1 second, and prints anything it receives back.
- The **Arduino** echoes back any command it receives (converted to uppercase), and independently sends its own status message every 3 seconds.
- Both sides use **non-blocking timing** (`millis()` / `time.time()`) instead of `delay()`/`sleep()`-based blocking, so they stay responsive to incoming data while also running periodic tasks.

## Full Code

### `pi_serial.py` (Raspberry Pi / Ubuntu)

```python
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
```

### `arduino_serial.ino` (Arduino)

```cpp
unsigned long lastTimeMessageSent = millis();

void setup() {
  Serial.begin(115200);
  while(!Serial){}
  while(Serial.available()>0){
  Serial.read();
  }
}

void loop() {
  if (Serial.available()>0){
    String cmd = Serial.readStringUntil('\n');
    cmd.toUpperCase();
    Serial.println(cmd);
  }

  unsigned long timeNow = millis();

  if(timeNow - lastTimeMessageSent>=3000){
    lastTimeMessageSent = timeNow;
    Serial.println("massage sent every 3 seconds");
  }

}


## How to run

1. The Arduino connected via USB, appearing as `/dev/ttyACM0` (adjust the port name in the script if yours differs, e.g. `/dev/ttyUSB0`)
2. Upload `arduino_serial.ino` to the Arduino using the Arduino IDE.
3. Connect the Arduino to the Pi via USB.
4. Run the Python script:
   ```bash
   python3 pi_serial.py
   ```
5. Press `Ctrl+C` to stop — the script closes the serial port cleanly on exit.

## Code Walkthrough

### Python — Connection retry loop

```python
while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        ...
        break
    except serial.SerialException:
        ...
```

Keeps attempting to open the serial port until it succeeds, instead of crashing if the Arduino isn't plugged in yet or isn't ready. `timeout=1.0` means read calls give up after 1 second if no data arrives, rather than blocking forever.

The `time.sleep(1)` and `ser.reset_input_buffer()` right after a successful connection exist because opening a serial port resets most Arduino boards (via the DTR line toggling the reset pin). The pause gives the board time to reboot and reach a stable state, and the buffer reset clears out any leftover garbage bytes generated during that reset.

### Python — Main loop

```python
while True:
    time.sleep(0.01)
    if ser.in_waiting > 0:
        msg = ser.readline().decode('utf-8').rstrip()
        print(msg)

    time_now = time.time()
    if time_now - last_time_vmd_send > 1.0:
        last_time_vmd_send = time_now
        ser.write("test'\n".encode('utf-8'))
```

- `ser.in_waiting`: number of bytes currently sitting in the input buffer, waiting to be read (Python's equivalent of Arduino's `Serial.available()`).
- `ser.readline()`: reads bytes up to a newline. Returns raw `bytes`, so `.decode('utf-8')` converts it to a string, and `.rstrip()` trims trailing whitespace/newline characters.
- `ser.write(...)`: sends data out. Python's `serial.write()` requires bytes, not a string, hence `.encode('utf-8')`.
- `last_time_vmd_send` / `time.time()`: the Python-side equivalent of the Arduino's `millis()` timer pattern — tracks elapsed time so a message is sent roughly once per second without blocking the loop.
- `time.sleep(0.01)`: a short pause each cycle to avoid pegging the CPU at 100% in a tight loop with nothing to wait on.

### Python — Clean shutdown

```python
except KeyboardInterrupt:
    print("Closing Serial Communication")
    ser.close()
```

Catches `Ctrl+C` and closes the serial port properly instead of leaving it open/locked when the script exits.

### Arduino — `setup()`

```cpp
Serial.begin(115200);
while(!Serial){}
while(Serial.available()>0){ Serial.read(); }
```

- `Serial.begin(115200)`: starts serial communication at 115200 baud (must match the baud rate used in the Python script).
- `while(!Serial){}`: waits until the serial connection is ready (mainly relevant on native-USB boards).
- `while(Serial.available()>0){ Serial.read(); }`: clears out any stray bytes left in the input buffer from the reset/connection process, so the sketch starts with a clean buffer.

### Arduino — `loop()`

```cpp
if (Serial.available()>0){
    String cmd = Serial.readStringUntil('\n');
    cmd.toUpperCase();
    Serial.println(cmd);
}
```

Checks if a full command has arrived, reads it up to the newline, converts it to uppercase, and echoes it back — this is what causes `"test"` sent from the Pi to come back as `"TEST"`.

```cpp
unsigned long timeNow = millis();
if(timeNow - lastTimeMessageSent >= 3000){
    lastTimeMessageSent = timeNow;
    Serial.println("massage sent every 3 seconds");
}
```

`lastTimeMessageSent` is declared as a **global variable** (outside `loop()`) so its value persists across iterations. `millis()` returns milliseconds elapsed since the Arduino started. This block checks whether 3000ms have passed since the last status message, and if so, sends one and resets the timer — all without blocking the rest of `loop()` (unlike using `delay(3000)`, which would freeze the whole program and make it unable to respond to incoming serial data during that time).

## Known Issues / Notes

- The Python script has a small typo in the message it sends: `"test'\n"` includes a stray apostrophe (should be `"test\n"`).
- The port `/dev/ttyACM0` is hardcoded; if another USB serial device is connected first, the Arduino may enumerate as `/dev/ttyACM1` instead.
- The Arduino's "massage sent every 3 seconds" message also has a typo (should be "message").

