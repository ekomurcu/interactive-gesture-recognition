import ipywidgets as widgets
import cv2
import numpy as np
from IPython.display import clear_output
from numpy import genfromtxt

hand_conditions = ["open_palm",
             "open_dorsal",
             "fist_palm",
             "fist_dorsal",
             "three_fingers_palm",
             "three_fingers_dorsal"]


hand_data = genfromtxt('interactive-gesture-recognition/dataset/Dataset_Subsystem_2.csv',str, delimiter=',')
hand_data = np.delete(hand_data,0,0)


def landmark_pairs(lndmrk):
    counter = 1
    lndmrk_pairs = []
    if float(lndmrk[0][0]) != 0.0 and float(lndmrk[0][1]) != 0.0:
        if float(lndmrk[1][0]) != 0.0 and float(lndmrk[1][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[0],lndmrk[1]])
        if float(lndmrk[4][0]) != 0.0 and float(lndmrk[4][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[0],lndmrk[4]])
        if float(lndmrk[8][0]) != 0.0 and float(lndmrk[8][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[0],lndmrk[8]])
        if float(lndmrk[12][0]) != 0.0 and float(lndmrk[12][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[0],lndmrk[12]])
        if float(lndmrk[16][0]) != 0.0 and float(lndmrk[16][1] != 0.0):
            lndmrk_pairs.append([lndmrk[0],lndmrk[16]])
        

    for i in range(2):
        if float(lndmrk[counter][0]) != 0.0 and float(lndmrk[counter][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[counter],lndmrk[counter+1]])
        counter += 1
    counter += 1
    for x in range(4):
        for i in range(3):
            if float(lndmrk[counter][0]) != 0.0 and float(lndmrk[counter][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0:
                lndmrk_pairs.append([lndmrk[counter],lndmrk[counter+1]])
            counter += 1
        counter += 1
            
    if float(lndmrk[20][0]) != 0.0 and float(lndmrk[20][1]) != 0.0:
        if float(lndmrk[21][0]) != 0.0 and float(lndmrk[21][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[20],lndmrk[21]])
        if float(lndmrk[24][0]) != 0.0 and float(lndmrk[24][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[20],lndmrk[24]])
        if float(lndmrk[28][0]) != 0.0 and float(lndmrk[28][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[20],lndmrk[28]])
        if float(lndmrk[32][0]) != 0.0 and float(lndmrk[32][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[20],lndmrk[32]])
        if float(lndmrk[36][0]) != 0.0 and float(lndmrk[36][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[20],lndmrk[36]])
        
    counter = 21
    for i in range(2):
        if float(lndmrk[counter][0]) != 0.0 and float(lndmrk[counter][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0:
            lndmrk_pairs.append([lndmrk[counter],lndmrk[counter+1]])
        counter += 1
    counter += 1
    for x in range(4):
        for i in range(3):
            if float(lndmrk[counter][0]) != 0.0 and float(lndmrk[counter][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0 and float(lndmrk[counter+1][1]) != 0.0:
                lndmrk_pairs.append([lndmrk[counter],lndmrk[counter+1]])
            counter += 1
        counter += 1

    return(lndmrk_pairs)

print("ok")