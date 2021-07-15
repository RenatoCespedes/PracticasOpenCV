import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math

def op_exp(img,b,c):
    if img is not None:
        col=['r','g','b']
        for i in range(len(img[0][0])):
            h=cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.show()
        
        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)

        #aplicamos el Histogram equalization en los 3 canales
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                for k in range(img.shape[1]):
                    vtmp=c*((b**img[j][k][i])-1)
                    if vtmp>255:
                        vtmp=255
                    if vtmp<0:
                        vtmp=0
                    out[j][k][i]=vtmp

        

        return(out,True)

    else:
        return(None,False)

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
        

def run_exp(folder,b,c):
    #Procesamos todos los elementos de la carpeta indicada
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        out,ok=op_exp(img,b,c)
        if ok:
            cv2.imwrite('./out3/out_exp'+str(b)+'-'+str(c)+'_'+filename,out)
    final_frame = cv2.hconcat((img, out))
    cv2.imshow('Exponencial',final_frame)
    cv2.waitKey(0)

def run_rtp(folder,c,r):
    #Procesamos todos los elementos de la carpeta indicada
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        out,ok=op_rtp(img,c,r)
        if ok:
            cv2.imwrite('./out3/out_rtp'+str(c)+'-'+str(r)+'_'+filename,out)
    final_frame = cv2.hconcat((img, out))
    cv2.imshow('Raise to Power',final_frame)
    cv2.waitKey(0)    

val1=1
val2=10
# for i in range(20):
#     print("valor b= "+ str(val1))
#     # print("valor c= "+ str(val2))
#     run_exp('./input1_3',val1,20)
#     val1=val1+0.01
    # val2=val2+0.01
# for i in range(21):
#     print("valor b= "+ str(val2))
#     # print("valor c= "+ str(val2))
#     run_exp('./input1_3',1.02,val2)
#     val2=val2+0.5

##
run_exp('./input1_3',1.015,10) # <- Operador B optimo para
# run_rtp('./input1_3',0.065,1.5) #  <- r optimo para operar
##