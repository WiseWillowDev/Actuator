import serial
import time
arduinoData = serial.Serial('/dev/ttyUSB0',115200)
time.sleep(1)
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
    print("{ Acal =",Acal," Gcal =",Gcal," Mcal =",Mcal," Scal =",Scal,"}, { pitch =",pitch," roll =",roll," yaw =",yaw, "}")