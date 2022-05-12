import serial, time

def progressif(ser, angle):
	angle = 361
	while angle > 180:
		ser.write(str(angle).encode())
		print(angle, "envoyé")
		time.sleep(0.05)
		angle -= 1
	return

def anyCommand(ser):
	while True:
		msg = input()
		if (msg == 'H'):
			ser.write(msg.encode())
			print(msg, "envoyé")
			print(ecoute(ser).rstrip("\n")," recu depuis la liaison série")
		else:
			ser.write(msg.encode())
			print(msg, "envoyé")
    			

def ecoute(ser):
    return ser.readline().decode()

ser = serial.Serial('COM5',19200) # /dev/ttyUSB0

# Décommenter la ligne en dessous pour pouvoir réaliser 
# 	un mouvement progressif horizontal du bras
# progressif(ser, angle)

# Décommenter la ligne ci-dessous pour rentrer une 
# 	consigne d'angle à trois chiffres
# anyCommand(ser)
msg = input()
ser.write(msg.encode())
print(msg, "envoyé")