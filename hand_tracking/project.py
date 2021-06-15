import numpy as np
import cv2
import time
import HandTrackingModule as htm
import pyautogui

####################################################################
wCam, hCam = 1280, 720
####################################################################

detector = htm.handDetector(maxHands=1, detectionCon=0.75)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if len(lmList):
        fingers = detector.fingersUp()
        if fingers[0] and fingers[1] and fingers[4]:
            thumb = lmList[4][1:]
            index = lmList[8][1:]
            middle = lmList[12][1:]
            ring = lmList[16][1:]
            pinky = lmList[20][1:]
            



    cv2.imshow('img', img)
    cv2.waitKey(1)

