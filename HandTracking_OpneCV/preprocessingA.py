import numpy as np
import cv2
import HandTrackingModule as htm
import os
import time
import datetime

####################################################################
# webcam 화면 사이즈 조정 파라미터
wCam, hCam = 1280, 720
####################################################################

detector = htm.handDetector(min_detection_confidence=0.75)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# model input값 초기화 이하 Canvas
Canvas = np.zeros((720, 1280, 3), np.uint8)
input_arr = []  # frame 저장 변수


img_path = './img'

########
prev_time = 0
FPS = 60
########

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    landmark_list, bbox = detector.findPosition(img, draw=False)
    # curr_time = time.time() - prev_time
    # if (success is True) and (curr_time > 1. / FPS):
    #     prev_time = time.time()

    # 손 인식이안되면 input_arr를 확인
    # 명령어를 입력하고 떠난 손동작에 대해서는 이미지생성.
    # input_arr에 데이터가 없으면 계속 landmark_list를 확인.
    if len(landmark_list) == 0:
        # input_arr에 데이터가 있으면 이미지 파일 생성후 전달.
        if input_arr: 
            prev_x, prev_y = input_arr[0]
            trans_color = 5  # 색 변화를 위해
            for i in input_arr:
                curr_x, curr_y = i
                cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, trans_color), 15)
                prev_x, prev_y = curr_x, curr_y
                if trans_color < 255:
                    trans_color += 25
                else:
                    trans_color = 255

            # output값을 보기 위한 png파일 변환
            t = datetime.datetime.now().strftime("%Y-%M-%d %H-%M-%S")
            cv2.imwrite(os.path.join(img_path, f'{t}.png'), Canvas)

            Canvas = np.zeros((720, 1280, 3), np.uint8)  # Canvas 초기화
            input_arr.clear()

    else:
        input_arr.append(landmark_list[8][1:])
    cv2.imshow('img', img)
    cv2.waitKey(1)