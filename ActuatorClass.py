import RPi.GPIO as GPIO
import time

class Actuator:
    
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        
    def setBoard(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        
    def setPins(self):
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        
    def noMovement(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)

    def up(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
                              
    def down(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()
        
    def wait(self):
        time.sleep(2)
