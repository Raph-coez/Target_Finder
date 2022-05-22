# main.py
from header import *

# Initialisation
print('Demarrage du programme principal ***************')
vs = VideoStream(src=0).start()
sleep(1)
detector = get_detector()
ser = serial.Serial('COM5',19200)
consignes_init = [str(ANGLE)+'F',LUMIERE_FALSE,str(ANGLE_VERTICAL)+'F']
init_position(ser,consignes_init,"Remise a l'angle initial vertical et horizontal, exctinction de la lumiere")
p = False

# Loop
while check_searching_target():
	COUNT += 1
	gray_img, frame = print_camera(vs)
	detected, rect = check_detection(detector, gray_img)
	distance = set_data(rect, frame)
	if not p:
		p = horizontal_target(detected, ser)
	#if p: 
		#pointeur_pos, detect = get_pointeur_center(gray_img)
		#vertical_target(pointeur_pos,detect, ser)
	if detected:
		vertical_target_2(distance, ser)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
	
# Close
print('Arret du programme principal ***********')
cv2.destroyAllWindows()
vs.stop()