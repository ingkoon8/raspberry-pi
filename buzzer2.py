import RPi.GPIO as GPIO
import time


SW1=5
BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(SW1, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

p=GPIO.PWM(BUZZER,391)
p.stop()

oldSw=0
newSw=0


try:
    while True:
        newSw = GPIO.input(SW1)
        if newSw != oldSw:
            oldSw = newSw

            # 스위치가 입력되면 391Hz의 부저를 두번 울림
            if newSw == 1:
                p.start(50)
                p.ChangeFrequency(391)
                time.sleep(0.2)

                p.stop()
                time.sleep(0.1)

                p.start(50)
                p.ChangeFrequency(391)
                time.sleep(0.2)

                p.stop()
                time.sleep(0.1)
        time.sleep(0.2)



except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
