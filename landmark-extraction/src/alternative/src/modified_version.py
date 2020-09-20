import cv2
import numpy as np
import matplotlib.pyplot as plt
import load_data as load
import explore_image as exp


def modified_extract_landmarks(n_points, frame_copy, frame_width, frame_height, output, threshold=0.1):
    # Empty list to store the detected key-points
    points = []
    landmarks = []
    n_points=22
    count=0
    for i in range(n_points):
        # confidence map of corresponding body's part.
        prob_map = output[0, i, :, :]
        prob_map = cv2.resize(prob_map, (frame_width, frame_height))

        # Find global maximum of the prob_map.
        min_val, prob, min_loc, point = cv2.minMaxLoc(prob_map)

        if prob > threshold :
            if i==0 or i>1:
                cv2.circle(frame_copy, (int(point[0]), int(point[1])), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)

                if i>1:
                    no=i-1
                else:
                    no=i

                #print(no,int(point[0]), int(point[1]))
                landmarks.append((count,int(point[0]), int(point[1])))
                cv2.putText(frame_copy, "{}".format(count), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 255), 2, lineType=cv2.LINE_AA)
                count+=1
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(point[0]), int(point[1])))
        else :
            points.append(None)

    plt.figure(figsize=[10,10])
    plt.imshow(cv2.cvtColor(frame_copy, cv2.COLOR_BGR2RGB))
    plt.show()
    cv2.imshow('Output-Key-points.jpg', frame_copy)
    cv2.waitKey(0)

    return landmarks

def modified_hand_extraction(frame, n_points, verbose=0):
    net=load.init()
    [frame_copy, frame_width, frame_height, output]=  exp.explore_frame(frame, net)
    if verbose:
        probMap= exp.visualise_prob(frame, output)
    landmarks = modified_extract_landmarks(n_points, frame_copy, frame_width, frame_height, output)
    return landmarks