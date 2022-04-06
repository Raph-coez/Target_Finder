# Fonction permettant de tester le retour caméra

import cv2
#import matplotlib.pyplot as mplot
#import numpy as np
#from algos_TOR import *

cam = cv2.VideoCapture(0)
screen_name = 'Processed Cam'
cv2.namedWindow('Processed Cam', cv2.WND_PROP_FULLSCREEN)
while True:
    ret, image = cam.read()
    if ret:
        cv2.imshow(screen_name, image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print('Aucun retour camera')
        break