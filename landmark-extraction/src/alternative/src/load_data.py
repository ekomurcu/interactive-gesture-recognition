import cv2


def init():
    proto_file = "../model/pose_deploy.prototxt"
    weights_file = "../model/pose_iter_102000.caffemodel"
    n_points = 22  # this should be 20 as max but it gives less when set.
    net = cv2.dnn.readNetFromCaffe(proto_file, weights_file)
    return net
