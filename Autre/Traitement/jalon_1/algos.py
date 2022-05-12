import matplotlib.pyplot as mplot
import numpy as np

def TOR_blue(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R < 0.5) and (img_G < 0.5) and (img_B > 0) and (img_I > 0.2)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img


    # TOR_cyan
def TOR_cyan(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R < 0.5) and (img_G < 1) and (img_B > 0.5) and (img_I > 0.8)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img



    # TOR_magenta
def TOR_magenta(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > 0.5) and (img_G < 0.3) and (img_B > 0.5) and (img_I > 0.8)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img

def TOR(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    taille = format[0] * format[1]
    count = 0
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > 0) and (img_G < 0.3) and (img_B > 0.4) and (img_I > 0.0)):
                new_img[i, j, 3] = 0
                count += 1
            else:
                new_img[i, j, 3] = 1
    if (count > 0):
        proportion = taille/count
    else:
        proportion = taille
    return new_img, proportion


def TOR_A(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    taille = format[0] * format[1]
    count = 0
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > 0) and (img_G < 0.3) and (img_B > 0.4) and (img_I > 0.0)):
                new_img[i, j, 3] = 0
                count += 1
            else:
                new_img[i, j, 3] = 1
    if (count > 0):
        proportion = taille/count
    else:
        proportion = taille
    return new_img, proportion

# Check_Prop : check la proportion de pixel blanc et en deduit la presence de la cible
def check_prop(prop):
    ret = ""
    if prop < 10:
        ret = "Cible reperee"
        print('Cible reperee pour n =  '+str(prop))
    else:
        ret = "Pas de cible"
        print('Cible non reperee, n = '+str(prop))
    return ret