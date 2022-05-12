    # Fichier permettant le traitement des images recues depuis le Rasberry

# Import des librairies / algos
import matplotlib.pyplot as plt
import matplotlib.image as pim
import numpy as np
import cv2
from algos import *

# Processing : choix de la methode de traitement
def Processing(img):
    return TOR_A(img)

# Periode de recuperation des images (ms)
T = 200

# Camera
cam = cv2.VideoCapture(0)

# Boucle d'affichage
while True:
    plt.figure(figsize=(14,8), dpi=80)
    ret, img = cam.read()
    if ret:
        copy_image = np.copy(img)
        pim.imsave('images/cam.png', img)
        img = plt.imread('images/cam.png')
        processed_img, prop = Processing(img)
        plt.subplot(121)
        plt.imshow(img)
        plt.title('Image non traitee')
        plt.axis('off')
        plt.subplot(122)
        plt.imshow(processed_img)
        plt.title("Image traitee : " + check_prop(prop))
        plt.axis('off')
        plt.show(False)
        plt.waitforbuttonpress()
        plt.close()
    else:
        print('Aucun retour camera')
        break
