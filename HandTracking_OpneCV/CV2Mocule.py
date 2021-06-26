import numpy as np
import cv2
import HandTrackingModule as htm
import os
import time
import datetime
import DataPreprocessing as dta

####################################################################
# webcam 화면 사이즈 조정 파라미터
wCam, hCam = 640, 360
####################################################################

detector = htm.handDetector(min_detection_confidence=0.75, max_num_hands=1)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# model input값 초기화 이하 Canvas
Canvas = np.zeros((hCam, wCam, 3), np.uint8)
input_arr = []  # frame 저장 변수
line_thickness = 3
line_color = (255, 255, 255)
finger_num = 8

########
prev_time = 0
FPS = 30
########

img_path = './img'
datapre = dta.datapreprocessing()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    landmark_list, bbox = detector.findPosition(img, draw=False)
    curr_time = time.time() - prev_time
    # 초당 프레임수 제한.
    if (success is True) and (curr_time > 1. / FPS):
        prev_time = time.time()
        datapre.datapreprocess(landmark_list)

    cv2.imshow('img', img)
    cv2.waitKey(1)
