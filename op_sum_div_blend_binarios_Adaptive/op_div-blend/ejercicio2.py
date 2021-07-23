import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math
def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

def op_division(img,img2):
    if img is not None and img2 is not None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        #extraccion de valores minimos y maximos
        mini=np.min(img)
        maxi=np.max(img)
        newmin=np.min(img2)
        newmax=np.max(img2)
        #ajustamos el tamaño de la imagen 2 a la de la imagen 1
        img2=cv2.resize(img2, (img.shape[1], img.shape[0]))

        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)
        #constante
        const=190

        for j in range(img.shape[0]):
            for k in range(img.shape[1]):
                out[j][k]=((((img[j][k]/img2[j][k])*const)-mini)*((newmax-newmin)/(maxi-mini)))+newmin

        show_img=hconcat_resize_min([img,img2,out])                
        cv2.imshow('Operacion division',show_img)
        cv2.waitKey()
        return(out)
    else:
        return(None)

def run_div(file1,file2):
    img = cv2.imread(file1)
    img2=cv2.imread(file2)
    out=op_division(img,img2)
    if out is not None:
        cv2.imwrite('./out1/out_div_1.jpg',out)
    
run_div('./input1/sub_1.jpg','./input1/sub_2.jpg') 
