import serial

ser = serial.Serial('COM5',19200)
while(True):
    a = input('Rentrez une commande \n')
    ser.write(a.encode())
    print('Commande envoyee. Rentrez une nouvelle commande \n')