import cv2
import os

def proccess_image(filename):
    img = cv2.imread(filename)
    result = cv2.convertScaleAbs(img, alpha=1.8, beta=30)
    name = os.path.splitext(filename)
    new_name = name[0] + "-after" + name[1]
    cv2.imwrite(new_name, result)

    return new_name