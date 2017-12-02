import serial

class Serial:
    ser = None

    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0")
        self.ser.baudrate = 115200

    def __del__(self):
        self.ser.close()

    def write(data):
        self.ser.write(data)
        return

    def receive(self, num):
        data = self.ser.read(num)
        return data
