import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math

def pixel(lst):
    return((float(lst[0])+float(lst[1])+float(lst[2]))/3)


def run(folder):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            ll=[]
            for i in range(len(img[0][0])):
                h=cv2.calcHist([img], [i], None, [256], [0, 256])

                ph=[0]*256
                for i in range (len(h)):
                    ph[i]=h[i]/(img.shape[0]*img.shape[1])
                
                sn=[]
                for i in range(256):
                    t=0
                    for i in range(i):
                        t+=ph[i]
                    sn.append(math.floor(256*t))
                ll.append(sn)
            
            #nueva imagen
            out=np.zeros(shape=img.shape,dtype=np.uint8)

            #aplicamos el Histogram equalization en los 3 canales
            for i in range(len(img[0][0])):
                for j in range(img.shape[0]):
                    for k in range(img.shape[1]):
                        out[j][k][i]=ll[i][img[j][k][i]]


            hf = cv2.calcHist([out], [0], None, [256], [0, 256])
            plt.plot(hf)
            
            final_frame = cv2.hconcat((img, out))
            cv2.imshow('Antes - Despues',final_frame)
            plt.show()
            cv2.waitKey()

            cv2.imwrite('./out/out_'+filename,out)

run('./imput')