# main.py
from header import *

# Initialisation
vs = VideoStream(src=0).start()
sleep(1)
detector = get_detector()
ser = serial.Serial('COM5',19200)
consignes_init = [str(ANGLE)+'F',LUMIERE_FALSE]
init_position(ser,consignes_init,"Remise a l'angle initial, exctinction de la lumiere")

# Loop
while SEARCHING_TARGET:
	COUNT += 1
	gray_img, frame = print_camera()
	detected, rect = check_detection(detector, gray_img)
	distance = set_data(rect, frame)
	horizontal_target(detected, ser)
	pointeur_pos, detect = get_pointeur_center(gray_img)
	#vertical_target(pointeur_pos,detect, ser)
	# suite : vertical_target(pointeur_pos)
	# vertical target
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
	
# Close
print('Arret du programme principal')
cv2.destroyAllWindows()
vs.stop()