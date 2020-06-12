import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

wait = 1


in1 = 31
in2 = 33

# A MOTOR
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

in3 = 35
in4 = 37

# B MOTOR
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

print ("starting")
print ("no movement")
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

time.sleep(wait)
print ("3 is high")
print ("B Motor is moving up")
GPIO.output(in3, GPIO.HIGH)
GPIO.output(in4, GPIO.LOW)

time.sleep(wait)
print ("4 is high")
print ("B MOTOR is moving down")
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.HIGH)
time.sleep(wait)

print ("motor A")
print ("1 is high")
print ("A Motor is moving up")
GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)
time.sleep(wait)

print ("2 is high")
print ("A Motor is moving down")
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
time.sleep(wait)

print ("together up")

GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)

GPIO.output(in3, GPIO.HIGH)
GPIO.output(in4, GPIO.LOW)
time.sleep(wait)

print ("together down")

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)

GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.HIGH)
time.sleep(wait)
print ("end")
GPIO.cleanup()