import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.7,
                      min_tracking_confidence=0.7)

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # 이미지 반전.
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for idx, lm in enumerate(handLms.landmark):
                # print(idx, lm) # 손표시 점의 idx와 좌표.
                h, w, c = img.shape
                centerX, centerY = int(lm.x * w), int(lm.y * h)
                print(idx, centerX, centerY)  # center의 좌표.

                if idx == 8:  # idx = 손점의 순서. 0 = 손바닥 4 = 엄지끝.
                    cv2.circle(img, (centerX, centerY), 10, (255, 0, 0), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime  # fps calculate

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 0), thickness=2)  # dispaly

    cv2.imshow("image", img)
    cv2.waitKey(1)
