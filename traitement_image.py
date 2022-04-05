    # Fichier permettant le traitement des images recues depuis le Rasberry

# Import des librairies
import matplotlib.image as mpimg
import matplotlib.pyplot as mplot
import numpy as np
import cv2

img = mpimg.imread('images/image_1.png')
mplot.imshow(img)
#mplot.show()