import numpy as np
import cv2
import HandTrackingModule as htm
import os
import time
import datetime

detector = htm.handDetector(min_detection_confidence=0.75)
wCam, hCam = 640, 360
videos = './videos/WIN_20210615_08_54_54_Pro.mp4'

cap = cv2.VideoCapture(videos)
# cap.set(3, wCam)
# cap.set(4, hCam)

####################################################################
# webcam 화면 사이즈 조정 파라미터

####################################################################

# model input값 초기화 이하 Canvas
Canvas = np.zeros((hCam, wCam, 3), np.uint8)
input_arr = []  # frame 저장 변수

########
prev_time = 0
FPS = 30
########
FPS = cap.get(cv2.CAP_PROP_FPS) # 영상의 FPS값 조회
delay_time = int(np.round(1000/FPS))

img_path = './img'
file_name_cnt = 0  # img파일 이름 중복 방지

while True:
    success, img = cap.read()
    # img = cv2.resize(img, dsize=(640,360), interpolation=cv2.INTER_AREA)
    # img = cv2.flip(img, 1)
    if success:
        img = detector.findHands(img)
        landmark_list, bbox = detector.findPosition(img, draw=False)

        curr_time = time.time() - prev_time
        # 초당 프레임수 제한.
        if (success is True) and (curr_time > 1. / FPS):
            prev_time = time.time()

            # 손 인식이 안되면 input_arr 초기화
            if len(landmark_list) == 0:
                if input_arr:
                    prev_x, prev_y = input_arr[0]
                    trans_color = 5  # 색 변화를 위해
                    for i in range(len(input_arr)):
                        # curr_x, curr_y = i
                        # cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, trans_color), 15)
                        # prev_x, prev_y = curr_x, curr_y
                        # if trans_color < 255:
                        #     trans_color += 25
                        # else:
                        #     trans_color = 255
                        if i < 5:
                            curr_x, curr_y = input_arr[i]
                            cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, trans_color), 15)
                            prev_x, prev_y = curr_x, curr_y
                        else:
                            curr_x, curr_y = input_arr[i]
                            cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, 255), 15)
                            prev_x, prev_y = curr_x, curr_y


                    # output값을 보기 위한 png파일 변환
                    t = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

                    cv2.imwrite(os.path.join(img_path, f'{t}.png'), Canvas)

                    Canvas = np.zeros((hCam, wCam, 3), np.uint8)  # Canvas 초기화
                    input_arr.clear()

            # 손 인식 되면 input_arr에 넣기
            else:
                if len(input_arr) < 30:
                    input_arr.append(landmark_list[8][1:])
                # input_arr 길이가 40이면  Canvas에 그리기
                if len(input_arr) == 30:
                    prev_x, prev_y = input_arr[0]
                    trans_color = 5  # 색 변화를 위해
                    for i in range(1, 30):
                        # curr_x, curr_y = input_arr[i]
                        # cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, trans_color), 15)
                        # prev_x, prev_y = curr_x, curr_y
                        # if trans_color < 255:
                        #     trans_color += 25
                        # else:
                        #     trans_color = 255
                        if i < 5:
                            curr_x, curr_y = input_arr[i]
                            cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, trans_color), 15)
                            prev_x, prev_y = curr_x, curr_y
                        else:
                            curr_x, curr_y = input_arr[i]
                            cv2.line(Canvas, (prev_x, prev_y), (curr_x, curr_y), (255, 0, 255), 15)
                            prev_x, prev_y = curr_x, curr_y

                    # output값을 보기 위한 png파일 변환
                    t = datetime.datetime.now().strftime("%Y-%M-%d %H-%M-%S")
                    print(type(Canvas), Canvas, Canvas.shape)
                    cv2.imwrite(os.path.join(img_path, f'{t}.png'), cv2.flip(Canvas,1))
                    # file_name_cnt += 1
                    Canvas = np.zeros((hCam, wCam, 3), np.uint8)  # Canvas 초기화

                    # 먼저 들어온 데이터 빼기(수정 필요)
                    input_arr = input_arr[10:]
    cv2.imshow('img', img)
    cv2.waitKey(1)