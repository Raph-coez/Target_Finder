# Modules

import matplotlib.pyplot as mplot
import numpy as np

# Fonctions de test
    # TOR_blue
def TOR_blue(a, b, c, d, img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R < a) and (img_G < b) and (img_B > c) and (img_I > d)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img

def TOR_magenta(a, b, c, d, img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > a) and (img_G < b) and (img_B > c) and (img_I > d)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img

# Test
img = mplot.imread('./images/test.png')
new_img = TOR_magenta(0.5,0.3,0.5,0.8,img)

# Affichage du test
mplot.subplot(121)
mplot.imshow(img)
mplot.axis('off')
mplot.title('Image a traiter')
mplot.subplot(122)
mplot.imshow(new_img)
mplot.axis('off')
mplot.title('Image traitee')
mplot.show()
