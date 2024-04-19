import serial
import time
import matplotlib.pyplot as plt
from pynput import keyboard
time.sleep(1)
bluetooth_serial_port = 'COM6'
baud_rate = 9600
evenement=""
print("Start")
port="COM6"  # This will be different for various devices and on Windows it will probably be a COM port.
bluetooth = serial.Serial(port, 9600)  # Start communications with the Bluetooth unit
print("Connected")

bluetooth.flushInput()  # This gives the Bluetooth a little kick
result = str(0)

def on_key_release(key):
    global result
    if result != 'stop':
        result = 'stop'
        result_bytes = result.encode('utf_8')
        bluetooth.write(result_bytes)

def on_key_pressed(key):
    global result
    result1 = '%s' % key
    if result == 'stop':
        if result1 == 'Key.up':
           result = 'forward'
        if result1 == 'Key.down':
           result = 'backwards'
        if result1 == 'Key.left':
           result = 'left'
        if result1 == 'Key.right':
           result = 'right'
        result_bytes = result.encode('utf_8')
        bluetooth.write(result_bytes)

x_vals = []
y_vals = []

plt.ion()  # Turn on interactive mode for Matplotlib

def read_data_from_arduino():
    data = b''  # Initialize an empty byte string to store incoming data
    while True:
        if bluetooth.in_waiting > 0:
            byte_data = bluetooth.read()  # Read a byte from the serial connection
            if byte_data == b'\n':  # Check if it's a newline character
                # Data received completely (assuming x,y format)
                xy_data = data.decode('utf-8').strip().split(',')
                if len(xy_data) == 2:
                    try:
                        x_val = float(xy_data[0])
                        y_val = float(xy_data[1])
                        x_vals.append(x_val)
                        y_vals.append(y_val)
                        plt.clf()  # Clear previous plot
                        plt.scatter(x_vals, y_vals, color='blue')
                        plt.xlabel('X')
                        plt.ylabel('Y')
                        plt.title('Robot Position')
                        plt.grid(True)
                        plt.xlim(-500, 500)  # Set X-axis limits to -1.5m to 1.5m
                        plt.ylim(-500, 500)  # Set Y-axis limits to -1.5m to 1.5m
                        plt.pause(0.01)  # Pause to update the plot
                    except ValueError:
                        print("Error parsing data:", data.decode('utf-8'))
                data = b''  # Reset data buffer for the next reading
            else:
                data += byte_data  # Append the byte to the data buffer

# Start a separate thread to continuously read data from Arduino
import threading
data_thread = threading.Thread(target=read_data_from_arduino)
data_thread.daemon = True  # Daemonize the thread so it stops with the main program
data_thread.start()

# Start listening for keyboard inputs
with keyboard.Listener(on_release=on_key_release, on_press=on_key_pressed) as listener:
    print("Ready for keyboard inputs...")
    listener.join()  # Wait for the listener thread to complete

# This part of the code is reached only after the keyboard listener exits
print("Exiting program")