import cv2
import numpy as np
import tensorflow as tf
import pandas as pd
from numpy import genfromtxt
import os
import matplotlib.pyplot as plt
from pandas import read_excel
import landmark_info as info
import load_images as load
from ipywidgets import interact, IntSlider

gestures = ["open_palm",
            "open_dorsal",
            "fist_palm",
            "fist_dorsal",
            "three_fingers_palm",
            "three_fingers_dorsal"]
# Loading excel file
# find your sheet name at the bottom left of your excel file and assign
# it to my_sheet
my_sheet = 'Tabelle1'  # change it to your sheet name
file_name = '../data/Video Data.xlsx'  # change it to the name of your excel file
df = read_excel(file_name, sheet_name=my_sheet)
df.head()  # shows headers with top 5 rows
# Gather landmarks information
# get_landmarks_info(get_ids(df), gestures)
# Display landmark columns for each gestures to see whether they are consistent or not.
info.print_nof_landmarks(info.get_ids(df), gestures)
# Start reading image
idd = info.get_ids(df)[6]
video_name = gestures[1]
img_path = "../img/" + str(idd) + "/" + str(video_name) + "/img_1.png"
print(img_path)
vid_path = "../videos/" + str(idd) + "/" + str(video_name) + ".webm"
print(vid_path)
img = cv2.imread(img_path)
print(img.shape)
load.display_image(img)
df_predicted=random_prediction(df)
df_predicted
evaluate(df, df_predicted, 100)

