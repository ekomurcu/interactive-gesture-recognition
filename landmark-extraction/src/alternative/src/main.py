import cv2
import time
import base_version as base
import modified_version as mod

# base.hand_extraction(cv2.imread('../img/hand.jpg'), 20)
# base.hand_extraction(cv2.imread('../img/right-frontal.jpg'), 20)
# base.hand_extraction(cv2.imread('../img/front-back.jpg'), 22)
# mod.modified_hand_extraction(cv2.imread('../img/hand.jpg'),22)
# base.hand_extraction(cv2.imread('../img/img_0.png'),22)
# base.hand_extraction(cv2.imread('../img/img_0.png'),20)
# mod.modified_hand_extraction(cv2.imread('../img/img_0.png'),22)
# base.hand_extraction(cv2.imread('../img/img_0.png'),16)
# mod.modified_hand_extraction(cv2.imread('../img/img_0.png'),18)
# base.hand_extraction(cv2.imread('../img/img_2.png'),22)
# mod.modified_hand_extraction(cv2.imread('../img/img_2.png'), 22)

for i in range(59):
    path = '../img/img_{}.png'
    print(base.hand_extraction(cv2.imread(path.format(i)), 22))
