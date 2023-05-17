import RPi.GPIO as GPIO
import time

SW1 = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 풀다운 저항을 설정하여 floating상태 제거

try:
    while True:
        sw1Value = GPIO.input(SW1)
        print(sw1Value)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
