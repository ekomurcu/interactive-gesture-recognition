import cv2
import os


def split_into_images(each_id, video_name):
    path = "../img/" + str(each_id) + "/" + str(video_name)
    try:
        os.mkdir("../img")
    except OSError as error:
        try:
            os.mkdir("../img/" + str(each_id))
        except OSError as error:
            try:
                os.mkdir(path)
            except OSError as error:
                dummy = 1
    foo = cv2.VideoCapture("../videos/" + str(each_id) + "/" + video_name + ".webm")
    ret, frame = foo.read()
    path += "/img_{}.png"

    counter = 0
    while ret:
        ret, frame = foo.read()
        if not ret:
            break

        location = path.format(counter)
        cv2.imwrite(path.format(counter), frame)
        counter += 1
    foo.release()
    return counter


def split_all(ids, gestures):
    for each_id in ids:
        for video_name in gestures:
            split_into_images(each_id, video_name)


def display_image(img):
    img_to_display = cv2.imencode('.png', img)[1].tostring()
    return widgets.Image(value=img_to_display)


