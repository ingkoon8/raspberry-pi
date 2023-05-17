import RPi.GPIO as GPIO
import time

BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

p=GPIO.PWM(BUZZER,261) # 주파수를 261Hz로 설정
p.start(50) # 50Duty로 실행

try:
    while True:
        p.start(50)
        p.ChangeFrequency(261)
        time.sleep(1.0)
        p.stop()
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
