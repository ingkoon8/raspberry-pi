import RPi.GPIO as GPIO
import time
PWMA = 18
AIN1 = 22
AIN2 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

# A채널은 자동차의 왼쪽 모터를 제어
L_Motor = GPIO.PWM(PWMA,500) # 500Hz로 세팅
L_Motor.start(0)

try:
    while True:
      # 모터를 자동차의 앞쪽으로 회전
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(10) # 듀티 사이클 10%로 세팅(힘이 약해서 모터가 돌지 않음)
        time.sleep(1.0)

        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(50) # 듀티 사이클 50%로 세팅
        time.sleep(1.0)

        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(100) # 듀티 사이클 100%로 세팅
        time.sleep(1.0)

        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(0) # 듀티 사이클 0%로 세팅
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
