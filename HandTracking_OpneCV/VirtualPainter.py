import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm
import datetime


####################
brushThickness = 15
eraserThickness = 100
###################

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(min_detection_confidence=0.85)
xp, yp =0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # 1. import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks.
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList) # 손의 랜드마크 출력.

        # tip of and middle fingers.
        x1, y1 = lmList[8][1:]  # 2번째 손가락 끝 좌표.
        x2, y2 = lmList[12][1:]  # 3번째 손가락끝

        # 3. Check Fingers are up.
        fingers = detector.fingersUp()
        print(fingers)
        # 4. if selection mode - Two fingers are up.
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            # Checking for the click
            print("selection")
            if y1 < 125: # less than header
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    drawColor = (255, 0, 0)
                    header = overlayList[1]
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), (255, 0, 255), cv2.FILLED)

        # 5. If Drawing mode - index finger is up.
        if fingers[1] and not fingers[2]:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            print("draw mode")

            if xp == 0 and yp == 0: # 그리는 포인트가 시작점일때.
                xp, yp = x1, y1


            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("imgGray", imgGray)# 그레이 128
    _, imgInv = cv2.threshold(imgGray, 30,255, cv2.THRESH_BINARY_INV) # convert into binary image
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)
    # img = cv2.addWeighted(img, 0.5,imgCanvas,0.5,0) # 이미지를 합쳐서 그리기. 캔버스의 이미지를 합친다.
    # img[0:125, 0:1280] = header # setting the header image

    cv2.imshow("imginv", imgInv)
    cv2.imshow("image", img)
    cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)
