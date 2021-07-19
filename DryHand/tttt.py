import pyautogui
import time


def test():
    pyautogui.press('win')
    time.sleep(0.1)
    pyautogui.write("chrome")
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.write("www.youtube.com")
    time.sleep(0.1)
    pyautogui.press('enter')


test()