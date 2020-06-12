import RPi.GPIO as GPIO
import time
from ActuatorClass import Actuator
from DualAcutatorClass import DualActuator

leftMotor = Actuator(31,33)

rightMotor = Actuator(35,37)

desk = DualActuator(leftMotor, rightMotor)

desk.setup()

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
       desk.up()
       time.sleep(0.2)
    if downState == GPIO.LOW:
       print ("down pressed")
       desk.down()
       time.sleep(0.2)
    if noState == GPIO.LOW:
       print ("no pressed")
       desk.noMovement()
       time.sleep(0.2)
        
        

