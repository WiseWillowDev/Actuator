import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def setup(button):
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

upPin = 11
downPin = 13
noPin = 15

buttons = [upPin, downPin, noPin]

for button in buttons:
    setup(button)

while True:
    upState = GPIO.input(upPin)
    downState = GPIO.input(downPin)
    noState = GPIO.input(noPin)
    if upState == GPIO.LOW:
       print ("up pressed")
       time.sleep(0.2)
    if downState == GPIO.LOW:
       print ("down pressed")
       time.sleep(0.2)
    if noState == GPIO.LOW:
       print ("no pressed")
       time.sleep(0.2)
        
        
