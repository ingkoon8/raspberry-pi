import serial
import threading
import time
import RPi.GPIO as GPIO

bluSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout = 1.0) # '/dev/ttyS0'는 serial0번, 통신속도 9600 timeout을 1.0초로 설정
gData = ' '

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

PWMA= 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

def motor_go(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(speed)

def motor_back(speed):
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    R_Motor.ChangeDutyCycle(speed)

def motor_right(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    R_Motor.ChangeDutyCycle(speed)

def motor_left(speed):
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(speed)

def motor_stop():
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(0)

# 쓰레드를 활용하여 통신기능 분리 - 딜레이에 의한 통신 주기가 틀어 것을 막아줌
def serial_thread(): 
    global gData
    while True:
        data=bluSerial.readline() # data값을 읽음
        data = data.decode() # 데이터의 bytes타입을 문자열 타입으로 decode
        gData = data

def main():
    global gData
    try:
        while True:
            if gData.find('go') >= 0:
                gData=' '
                print('ok go')
                motor_go(50)
            elif gData.find('back') >= 0:
                gData=' '
                print('ok back')
                motor_back(50)
            elif gData.find('left') >= 0:
                gData=' '
                print('ok left')
                motor_left(50)
            elif gData.find('right') >= 0:
                gData=' '
                print('ok right')
                motor_right(50)
            elif gData.find('stop') >= 0:
                gData=' '
                print('ok stop')
                motor_stop()
             
            # 스위치 입력을 통한 비상정지 기능
            if GPIO.input(SW1)==1 or GPIO.input(SW2) == 1 or GPIO.input(SW3) == 1 or GPIO.input(SW4) ==1:
                motor_stop()
                
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bluSerial.close()
    GPIO.cleanup()
