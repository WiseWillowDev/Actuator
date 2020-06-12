from ActuatorClass import Actuator
import time

class DualActuator:
    
    def __init__(self, leftMotor, rightMotor):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        
    def setup(self):
        self.rightMotor.setBoard()
        self.rightMotor.setPins()
        self.leftMotor.setPins()
        
    def noMovement(self):
        self.rightMotor.noMovement()
        self.leftMotor.noMovement()
        
    def up(self):
        self.rightMotor.up()
        self.leftMotor.up()
        
    
    def down(self):
        self.rightMotor.down()
        self.leftMotor.down()

    
    def wait(self, amount):
        time.sleep(amount)
    
    def cleanup(self):
        self.rightMotor.cleanup()
    
    