import cv2
import time
import numpy as np
import matplotlib.pyplot as plt


def explore_frame(frame, net):
    frame_copy = np.copy(frame)
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    aspect_ratio = frame_width / frame_height
    threshold = 0.05

    t = time.time()
    # input image dimensions for the network
    in_height = 368
    # inWidth = 368
    in_width = int(((aspect_ratio * in_height) * 8) // 8)
    in_blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (in_width, in_height),
                                    (0, 0, 0), swapRB=False, crop=False)

    net.setInput(in_blob)

    output = net.forward()
    return frame_copy, frame_width, frame_height, output


def visualise_prob(frame, output):
    for i in range(22):
        prob_map = output[0, i, :, :]
        prob_map = cv2.resize(prob_map, (frame.shape[1], frame.shape[0]))
        plt.figure(figsize=[14, 10])
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.imshow(prob_map, alpha=0.6)
        plt.colorbar()
        plt.axis("off")
        cv2.waitKey(0)
    return prob_map
