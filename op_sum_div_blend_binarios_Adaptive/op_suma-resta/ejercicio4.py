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

def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

def op_resta(img,img2):
    if img is not None and img2 is not None:

        #Se ajusta el tamaño de la imagen 2 a la de la imagen 1
        img2=cv2.resize(img2, (img.shape[1], img.shape[0]))

        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)

      
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                for k in range(img.shape[1]):
                    out[j][k][i]=abs(int(img[j][k][i])-int(img2[j][k][i]))

        show_img=concat_tile_resize([[img,img2],[out]])
        cv2.imshow('Sustracción de Imagenes',show_img)
        cv2.waitKey()
        return(out)

    else:
        return(None)

def run_exp(file1,file2):

    img = cv2.imread(file1)
    img2=cv2.imread(file2)
    out=op_resta(img,img2)
    if out is not None:
        cv2.imwrite('./out1/out_exercise4.jpg',out)



run_exp('./input1/sub_10.jpg','./input1/sub_11.jpg') 
