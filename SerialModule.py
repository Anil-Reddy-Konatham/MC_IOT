import time
import serial
from time import ctime
import glob
import threading
from commonutility import print_data as pd


class ConnectingSerialPort:
    threading = None

    def __init__(self):
        self.ser = self.SerialPortConnection()

    def SerialPortConnection(self):  # connecting to port
        try:
            port_dest = glob.glob('/dev/tty[A-Za-z]*')[0]
            ser = serial.Serial(port_dest, 115200, timeout=10)
            return ser
        except serial.SerialException as msg:
            pd('{} serial port connection error: '.format(str(msg)))
            time.sleep(1)

    def serial_read(self):  # Reading port
        while True:
            try:
                data = (self.ser.readline()).decode("utf-8").strip()
                if (len(data) > 5):
                    pd(data)
            except:
                pd('serial port is not able to decode this message')

    def serial_write(self, cmd1):  # writing to port
        try:
            self.ser.write(bytes(cmd1 + '\r\n', 'utf-8'))
            time.sleep(0.2)
        except:
            pd('stop')


if __name__ == '__main__':
    serial_auto = ConnectingSerialPort()
    threading.Thread(target=serial_auto.serial_read).start()
    serial_auto.serial_write('show bs phyconfig')
