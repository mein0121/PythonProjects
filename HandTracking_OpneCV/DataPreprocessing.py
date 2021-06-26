import numpy as np
import cv2
import HandTrackingModule as htm
import os
import time
import datetime


class datapreprocessing:

    def __init__(self):
        self.wCam = 640
        self.hCam = 360
        self.Canvas = np.zeros((self.hCam, self.wCam, 3), np.uint8)
        self.input_arr = []  # frame 저장 변수
        self.line_thickness = 3
        self.line_color = (255, 255, 255)
        self.finger_num = 8
        self.img_path = './img'

    def datapreprocess(self, landmark_list):
        if len(landmark_list) == 0:
            if self.input_arr:
                prev_x, prev_y = self.input_arr[0]
                for i in range(len(self.input_arr)):
                    curr_x, curr_y = self.input_arr[i]
                    cv2.line(self.Canvas, (prev_x, prev_y), (curr_x, curr_y), self.line_color, self.line_thickness)
                    prev_x, prev_y = curr_x, curr_y

                # output값을 보기 위한 png파일 변환
                t = datetime.datetime.now().strftime("%Y-%M-%d %H-%M-%S")
                cv2.imwrite(os.path.join(self.img_path, f'{t}.png'), self.Canvas)
                self.input_arr = self.input_arr[10:]
                self.Canvas = np.zeros((self.hCam, self.wCam, 3), np.uint8)  # Canvas 초기화

        # 손 인식 되면 input_arr에 넣기
        else:
            if len(self.input_arr) < 30:
                self.input_arr.append(landmark_list[self.finger_num][1:])
            # input_arr 길이가 30이면  Canvas에 그리기
            if len(self.input_arr) == 30:
                prev_x, prev_y = self.input_arr[0]
                trans_color = 5  # 색 변화를 위해
                for i in range(1, 30):
                    curr_x, curr_y = self.input_arr[i]
                    cv2.line(self.Canvas, (prev_x, prev_y), (curr_x, curr_y), self.line_color, self.line_thickness)
                    prev_x, prev_y = curr_x, curr_y

                # 추론 모델 불러오르는것 대신 이미지 출력.
                t = datetime.datetime.now().strftime("%Y-%M-%d %H-%M-%S")
                cv2.imwrite(os.path.join(self.img_path, f'{t}.png'), self.Canvas)
                self.input_arr = self.input_arr[10:]
                self.Canvas = np.zeros((self.hCam, self.wCam, 3), np.uint8)  # Canvas 초기화



