import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()  # (-128.0, -127.00390625, 0.00390625)
# volume.SetMasterVolumeLevel(-127.1, None)

minvol = volRange[0]
maxvol = volRange[1]

width, height = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
pTime = 0
vol = 0
volbar = 400
volper = 0

detector = htm.handDetector()

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]  # 엄지의 좌표
        x2, y2 = lmList[8][1], lmList[8][2]  # 검지의 좌표

        centerX, centerY = (x1 + x2) // 2, (y1 + y2) // 2  # 엄지와 검지사이의 중간좌표

        cv2.circle(img, (x1, y1), 5, (255, 255, 255), cv2.FILLED)  # 엄지
        cv2.circle(img, (x2, y2), 5, (255, 255, 255), cv2.FILLED)  # 검지

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)  # 엄지와 검지사이 라인긋기

        cv2.circle(img, (centerX, centerY), 3, (0, 0, 0), cv2.FILLED)  # 엄지 검지라인의 중간.

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # handrage: min=20, max=200
        # volrange: min=-128, max=-127

        vol = np.interp(length, [20, 200], [minvol, maxvol])
        volbar = np.interp(length, [20, 200], [400, 150])
        volper = np.interp(length, [20, 200], [0, 100])

        print(int(length), vol, volbar)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (centerX, centerY), 3, (0, 255, 255), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volper)}%', (40, 450), cv2.FONT_ITALIC, 1, (255, 255, 0), thickness=2)  # dispaly

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        break
