import serial

ser = serial.Serial('COM5',19200)
while(True):
    a = input('Rentrez une commande \n')
    #a += 'F'
    ser.write(a.encode())