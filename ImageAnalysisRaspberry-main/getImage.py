import cv2
import numpy
import matplotlib.image as mp


def getImage():

    # Acces a la camera
    cam = cv2.VideoCapture(0)
    count = 1
    while count <= 5:
        ret, image = cam.read()
        if cv2.waitKey(1500) &0xFF == ord('q'):
            break
        copy_image = numpy.copy(image)
        image_name = 'images/image_' + str(count) + '.png'
        mp.imsave(image_name, copy_image)
        count += 1