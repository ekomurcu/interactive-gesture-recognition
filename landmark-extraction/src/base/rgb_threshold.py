import cv2
import ipywidgets as widgets
from ipywidgets import interact, IntSlider

# RGB Threshold
disp = widgets.Image()


def threshold(img, lower, upper):
    mask = cv2.inRange(img, np.array(lower), np.array(upper))
    masked = cv2.bitwise_and(img, img, mask=mask)

    display_image = cv2.imencode('.png', masked)[1].tostring()
    disp.value = display_image


def threshold_rgb(img, lower, upper):
    img_rgb = img
    mask = cv2.inRange(img_rgb, np.array(lower), np.array(upper))
    masked = img.copy()  # cv2.bitwise_and(img, img, mask = mask)

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
    disp.value = display_image


def foo(lower_r, lower_g, lower_b, upper_r, upper_g, upper_b):
    lower = [lower_b, lower_g, lower_r]
    upper = [upper_b, upper_g, upper_r]
    threshold_rgb(img, lower, upper)
    display(lower, upper)


widgets.interact(foo,
                 lower_r=IntSlider(min=0, max=255, step=1, value=0),
                 lower_g=IntSlider(min=0, max=255, step=1, value=0),
                 lower_b=IntSlider(min=0, max=255, step=1, value=0),
                 upper_r=IntSlider(min=0, max=255, step=1, value=255),
                 upper_g=IntSlider(min=0, max=255, step=1, value=255),
                 upper_b=IntSlider(min=0, max=255, step=1, value=255))

display(disp)