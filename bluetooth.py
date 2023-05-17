import serial
import threading
import time

bluSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout = 1.0) # '/dev/ttyS0'는 serial0번, 통신속도 9600 time-out 1.0초로 설정
gData = ' '

def serial_thread():
    global gData
    while True:
        data=bluSerial.readline()
        data = data.decode()
        gData = data

def main():
    global gData
    try:
        while True:
            print('serial data:', gData)
            time.sleep(1.0)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bluSerial.close()



bluSerial.close()
