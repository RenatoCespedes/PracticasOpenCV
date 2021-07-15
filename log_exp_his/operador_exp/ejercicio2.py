import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math
import sys

def op_rtp(img,c,r):
    if img is not None:
        col=['r','g','b']
        for i in range(len(img[0][0])):
            h=cv2.calcHist([img], [i], None, [256], [0, 256])
        
        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)

        #aplicamos el Histogram equalization en los 3 canales
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                for k in range(img.shape[1]):
                    vtmp=c*((img[j][k][i])**r)
                    if vtmp>255:
                        vtmp=255
                    if vtmp<0:
                        vtmp=0
                    out[j][k][i]=vtmp
        return(out,True)
    else:
        return(None,False)

def run_rtp(folder,c,r):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        out,ok=op_rtp(img,c,r)
        if ok:
            cv2.imwrite('./out1_2/out_rtp'+str(c)+'-'+str(r)+'_'+filename,out)
            print("Imagen Transformada")
    final_frame = cv2.hconcat((img, out))
    cv2.imshow('Antes - Despues',final_frame)
    cv2.waitKey(1)

# val1=float(sys.argv[1])
# val2=float(sys.argv[2])
# for i in range(int(val2)+10):
#     print("valor b= "+ str(val2))
#     # print("valor c= "+ str(val2))
#     run_rtp('./input1_2',val1,val2)
#     val2=val2+0.05
run_rtp('./input1_2',0.065,1.65) #  <- r optimo para operar