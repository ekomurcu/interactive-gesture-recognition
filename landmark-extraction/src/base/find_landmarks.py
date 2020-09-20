from IPython.display import display
import cv2


def min_max_finder(best_contour):
    max_x=0
    max_y=0
    min_x=800
    min_y=700
    for row in range(len(best_contour)):
        min_x = min(min_x , best_contour[row][0][0])
        min_y = min(min_y , best_contour[row][0][1])

        max_x = max(max_x , best_contour[row][0][0])
        max_y = max(max_y , best_contour[row][0][1])
    return min_x, min_y, max_x, max_y
def pos_finder(best_contour, given, x_or_y):
    for row in range(len(best_contour)):
        if x_or_y==0 and best_contour[row][0][1]==given:
            return best_contour[row][0][0]
        elif x_or_y==1 and best_contour[row][0][0]==given:
            return best_contour[row][0][1]

def landmark_finder():

    foo = cv2.VideoCapture(vid_path)
    writer = cv2.VideoWriter("exercise8.mp4", cv2.CAP_ANY, cv2.VideoWriter_fourcc(*"X264"), 12, (2 * 640, 480))

    lower_hsv = [0, 28, 105]
    upper_hsv = [255, 255, 255]

    # lower_rgb = [114, 0, 0]
    # upper_rgb = [255, 255, 255]
    frame = img.copy()
    count = 0
    ret, frame = foo.read()
    while ret:
        ret, frame = foo.read()
        if not ret:
            break
        count += 1
        # if 1==1:
        # color threshold using HSV
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_hsv, np.array(lower_hsv), np.array(upper_hsv))
        masked_hsv = cv2.bitwise_and(frame, frame, mask=mask)

        # draw contours from HSV thresholding
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        max_idx = 0
        max_val = 0
        for idx, c in enumerate(contours):
            if cv2.contourArea(c) > max_val:
                max_idx = idx
                max_val = cv2.contourArea(c)

        # compute the center of the biggest contour
        cv2.drawContours(masked_hsv, contours[max_idx], -1, (255, 255, 255), 2)
        M = cv2.moments(contours[max_idx])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(masked_hsv, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(masked_hsv, "center", (cX - 20, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(masked_hsv, "HSV", (5, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

        cv2.putText(frame, "Original", (5, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
        # cv2.drawContours(frame, contours[max_idx], -1, (0, 0, 255), 2)
        min_x, min_y, max_x, max_y = min_max_finder(contours[max_idx])
        # print(min_x, min_y, max_x, max_y)
        cv2.rectangle(frame, (min_x, max_y), (max_x, min_y), (255, 0, 0), 2)

        x_max_y = pos_finder(contours[max_idx], max_y, 0)
        cv2.circle(frame, (x_max_y, max_y), 5, (0, 0, 255), -1)
        cv2.putText(frame, "root", (x_max_y - 20, max_y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        root = (x_max_y, max_y)

        x_min_y = pos_finder(contours[max_idx], min_y, 0)
        cv2.circle(frame, (x_min_y, min_y), 5, (0, 0, 255), -1)
        cv2.putText(frame, "M4", (x_min_y - 20, min_y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        m4 = (x_min_y, min_y)

        y_max_x = pos_finder(contours[max_idx], max_x, 1)
        cv2.circle(frame, (max_x, y_max_x), 5, (0, 0, 255), -1)
        cv2.putText(frame, "P4", (max_x - 20, y_max_x - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        p4 = (max_x, y_max_x)

        y_min_x = pos_finder(contours[max_idx], min_x, 1)
        cv2.circle(frame, (min_x, y_min_x), 5, (0, 0, 255), -1)
        cv2.putText(frame, "T3", (min_x - 20, y_min_x - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        t3 = (min_x, y_min_x)

        r4 = (int((p4[0] + m4[0]) / 2), int(5 * (p4[1] + m4[1]) / 12))
        cv2.circle(frame, r4, 5, (0, 0, 255), -1)
        cv2.putText(frame, "R4", (r4[0] - 20, r4[1] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        i4 = (int((t3[0] + m4[0]) / 2), r4[1])
        cv2.circle(frame, i4, 5, (0, 0, 255), -1)
        cv2.putText(frame, "I4", (i4[0] - 20, i4[1] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Draw line conjigent to T3
        cv2.line(frame, t3, (max_x, t3[1]), (0, 255, 0), 1)

        # Draw line connecting to root from fingers
        cv2.line(frame, t3, root, (0, 255, 255), 1)
        cv2.line(frame, i4, root, (0, 255, 255), 1)
        cv2.line(frame, m4, root, (0, 255, 255), 1)
        cv2.line(frame, r4, root, (0, 255, 255), 1)
        cv2.line(frame, p4, root, (0, 255, 255), 1)

        # cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)
        # cv2.putText(frame, "center", (cX - 20, cY - 20),
        #    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        frame_stacked = np.hstack([frame, masked_hsv])
        writer.write(frame_stacked)
        if count == 1:
            first_frame = frame_stacked
    foo.release()
    writer.release()
