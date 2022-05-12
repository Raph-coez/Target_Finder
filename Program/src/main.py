# import the necessary packages
from imutils.video import VideoStream
import argparse
# import imutils
import time
import cv2
import os
from math import exp,log
from correction_horizontale import *


#fonction pour raph
data = []
def getData():
	print(data)
	return(data)


#on doit donner en paramètre le chemin du dossier cascade
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str, help = "path to input directory containing haar cascades")
args = vars(ap.parse_args())

print("[INFO] loading haar cascades...")
detector = cv2.CascadeClassifier(args["cascade"])



#on allume la caméra (on attend 1 seconde le temps qu'elle soit fonctionnelle)
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(1)

processed = False

print("Démarrage du programme ...")

while True:

	data = [0,0]
	#on boucle sur le flux vidéo (on récupère les images)
	frame = vs.read()
	frame = cv2.resize(frame, (512, 384))
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('..\img\img.png',frame)

	# perform face detection using the appropriate haar cascade


	rect = detector.detectMultiScale( gray, scaleFactor=1.25, minNeighbors=1, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
	if rect == () or processed:
		detected = False
	else : 
		detected = True
 
 
	for (fX, fY, fW, fH) in rect:


		data = [fX,fW]

		cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)

		# print("Sommet du rectangle : ( %s , %s ), longueur : %s, largeur : %s" %(fX,fY,fW,fH)) #abscisses, ordonnée, longueur = largeur

		distance = int(13315*exp(-0.986*log(fH)))
		#a = [ 582.25 , -9.7464 , 0.0843, -4e-4 , 9e-7 , -8e-10 ]
		#distance = a[0]*fH**0 + a[1]*fH + a[2]*fH**2 + a[3]*fH**3 + a[4]*fH**4 - a[5]*fH**5 
		

		#if 40 < distance < 250:
			
			#print("Distance à la cible : %s cm" %(distance))	

		# Correction de l'angle :
		if(detected):
			print('Cible detectee')
			time.sleep(0.4)
			print('Correction...')
			im = cv2.imread('..\img\img.png',0)
			x,w = data[0],data[1]
			angle, processed = correction_horizontale(im,x,w)
			if processed:
				print('Cible atteinte')
				print("Arret de la correction d'angle horizontal")
			if (angle < 181 or angle > 359):
				print('Angle maximal atteint')
			else:
				set_angle(angle)
				print('Angle modifé')
		cv2.imshow("Frame", frame)


	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()