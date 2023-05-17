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

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

try:
    while True:
        
        # 모터가 자동차의 앞으로 회전
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(50) # 듀티사이클을 50%로 설정
        time.sleep(1.0)

        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(00) # 듀티사이클을 0%로 설정하여 정지
        time.sleep(1.0)

        # 모터가 자동차의 뒤로 회전
        GPIO.output(AIN1,1)
        GPIO.output(AIN2,0)
        L_Motor.ChangeDutyCycle(50) # 듀티사이클을 50%로 설정
        time.sleep(1.0)

        GPIO.output(AIN1,1)
        GPIO.output(AIN2,0)
        L_Motor.ChangeDutyCycle(50) # 듀티사이클을 50%로 설정하여 정지
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
