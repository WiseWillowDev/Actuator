import RPi.GPIO as GPIO
import time 
from ActuatorClass import Actuator
from threading import Thread

def motor1(actuator):
    print("here")
    actuator.setBoard()

    actuator.setPins()

    actuator.up()
    actuator.down()
    

if __name__ == '__main__':
 
    leftMotor = Actuator(31,33)

    rightMotor = Actuator(35,37)

    t1 = Thread(target = motor1, args=(rightMotor,))
    t2 = Thread(target = motor1, args=(leftMotor,))

    a = t1.start()
    b = t2.start()
    print ("done")
    rightMotor.cleanup()