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

def op_multi(img,c):
    if img is not None:

        #creamos una imagen en negro
        out=np.zeros(shape=img.shape,dtype=np.uint8)

        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                for k in range(img.shape[1]):
                    if int(img[j][k][i]*c)>255:
                        out[j][k][i]=255
                    else:
                        out[j][k][i]= int(img[j][k][i]*c)

        show_img=hconcat_resize_min([img,out])
        cv2.imshow('Multiplicacion x constante c= '+str(c),show_img)
        cv2.waitKey()
        return(out)
    else:
        return(None)

def run_exp(file1,c):
    img = cv2.imread(file1)
    out=op_multi(img,c)
    if out is not None:
        cv2.imwrite('./out1/out_mul_4_'+str(c)+'.jpg',out)
        

constantes=[2,5,7]
for i in constantes:
    run_exp('./input1/mul_4_2.jpg',i) 