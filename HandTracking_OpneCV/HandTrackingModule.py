import cv2
import mediapipe as mp
import tensorflow as tf
import time


class handDetector():
    def __init__(self, mode=False, max_num_hands=2,
                 min_detection_confidence=0.7,
                 min_tracking_confidence=0.7):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,
                                        self.max_num_hands,
                                        self.min_detection_confidence,
                                        self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        landmarkList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for idx, lm in enumerate(myHand.landmark):
                # print(idx, lm) # 손표시 점의 idx와 좌표.
                h, w, c = img.shape
                centerX, centerY = int(lm.x * w), int(lm.y * h)
                # print(idx, centerX, centerY)  # center의 좌표.

                landmarkList.append([idx,centerX,centerY])

                # if idx == 8:  # idx = 손점의 순서. 0 = 손바닥 4 = 엄지끝.
                if draw:
                    cv2.circle(img, (centerX, centerY), 3, (0, 0, 0), cv2.FILLED)

        return landmarkList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)  # 이미지 반전.
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4]) # 4번째 포인트 엄지손끝

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime  # fps calculate

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 0), thickness=2)  # dispaly

        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
