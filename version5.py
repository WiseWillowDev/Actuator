import RPi.GPIO as GPIO
import time
from ActuatorClass import Actuator
from DualAcutatorClass import DualActuator
import serial
import time
arduinoData = serial.Serial('/dev/ttyUSB0',115200)
time.sleep(1)

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
    
error = False    


while True:
    while (arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    splitPacket = dataPacket.split(',')
    Acal=float(splitPacket[0]);
    Gcal=float(splitPacket[1]);
    Mcal=float(splitPacket[2]);
    Scal=float(splitPacket[3]);
    pitch=float(splitPacket[4]);
    roll=float(splitPacket[5]);
    yaw=float(splitPacket[6]);
    if (roll > 2 or roll < -2):
        desk.noMovement()
        if error == False:
            print("error, desk is tilted")
        error = True
    else:
        if error == True:
            print("error is fixed")
        error = False
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
        
    


