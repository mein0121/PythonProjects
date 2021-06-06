import cv2
import mediapipe as mp
import tensorflow as tf
import time
import HandTrackingModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # 이미지 반전.
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        print(lmList[4])  # 4번째 포인트 엄지손끝

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime  # fps calculate

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 0), thickness=2)  # dispaly

    cv2.imshow("image", img)
    cv2.waitKey(1)