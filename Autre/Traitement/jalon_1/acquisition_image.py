    # Fichier permettant l'acquisition des images depuis le rasberry

import cv2
import numpy
import matplotlib.image as mp


# Acces a la camera
cam = cv2.VideoCapture(0)
count = 2001
while count <= 20000:
    ret, image = cam.read()
    if cv2.waitKey(10) &0xFF == ord('q'):
        break
    copy_image = numpy.copy(image)
    image_name = 'img/' + str(count) + '.png'
    mp.imsave(image_name, copy_image)
    count += 1