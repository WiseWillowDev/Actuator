from ActuatorClass import Actuator
from DualAcutatorClass import DualActuator

leftMotor = Actuator(31,33)

rightMotor = Actuator(35,37)

desk = DualActuator(leftMotor, rightMotor)

desk.setup()
for x in range(3):
    desk.up()
    desk.wait(2)
    desk.down()
    desk.wait(2)
desk.cleanup()