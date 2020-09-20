import cv2

disp2 = widgets.Image()
img = img_face_removed

def threshold_hsv(img, lower, upper):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, np.array(lower), np.array(upper))
    masked = cv2.bitwise_and(img, img, mask=mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    max_idx = 0
    max_val = 0
    for idx, c in enumerate(contours):
        if cv2.contourArea(c) > max_val:
            max_idx = idx
            max_val = cv2.contourArea(c)

    cv2.drawContours(masked, contours[max_idx], -1, (0, 0, 255), 2)
    M = cv2.moments(contours[max_idx])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(masked, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(masked, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    display_image = cv2.imencode('.png', masked)[1].tostring()
    disp2.value = display_image


def foo2(lower_H, lower_S, lower_V, upper_H, upper_S, upper_V):
    lower = [lower_H, lower_S, lower_V]
    upper = [upper_H, upper_S, upper_V]
    threshold_hsv(img, lower, upper)
    display(lower, upper)

    widgets.interact(foo2,
                     lower_H=IntSlider(min=0, max=255, step=1, value=0),
                     lower_S=IntSlider(min=0, max=255, step=1, value=0),
                     lower_V=IntSlider(min=0, max=255, step=1, value=0),
                     upper_H=IntSlider(min=0, max=255, step=1, value=255),
                     upper_S=IntSlider(min=0, max=255, step=1, value=255),
                     upper_V=IntSlider(min=0, max=255, step=1, value=255))