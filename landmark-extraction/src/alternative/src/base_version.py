import cv2
import explore_image as exp
import load_data as load


def extract_landmarks(n_points, frame_copy, frame_width, frame_height, output, threshold=0.1):
    points = []
    landmarks = []
    nPoints = 22
    count = 0
    for i in range(n_points):
        # confidence map of corresponding body's part.
        prob_map = output[0, i, :, :]

        prob_map = cv2.resize(prob_map, (frame_width, frame_height))
        # Find global maximum of the probMap.

        min_val, prob, min_loc, point = cv2.minMaxLoc(prob_map)

        if prob > threshold:

            cv2.circle(frame_copy, (int(point[0]), int(point[1])), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame_copy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2, lineType=cv2.LINE_AA)
            # Add the point to the list if the probability is greater than the threshold
            landmarks.append((count, int(point[0]), int(point[1])))
            points.append((int(point[0]), int(point[1])))
            count += 1
        else:
            points.append(None)

    #cv2.imshow('Output-Key-points', frame_copy)
    #cv2.waitKey(0)
    return landmarks


def hand_extraction(frame, n_points, verbose=0):
    net = load.init()
    [frame_copy, frame_width, frame_height, output] = exp.explore_frame(frame, net)
    if verbose:
        prob_map = exp.visualise_prob(frame, output)
    return extract_landmarks(n_points, frame_copy, frame_width, frame_height, output)
