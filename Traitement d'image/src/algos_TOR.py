import matplotlib.pyplot as mplot
import numpy as np

    # TOR_blue
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

