import pyautogui
import time
import datetime

print(pyautogui.position())
# pyautogui.moveTo(1652,359) # 마우스 움직임 (x,y, 시간)

# pyautogui.moveRel(0,300,2) # 현재위치에서 이동.
p = ['a', 'b', 'c', 'd']

# pyautogui.moveTo(1770,560)
# pyautogui.leftClick()
# pyautogui.write("Hello World")
# pyautogui.keyDown("a")
#
# pyautogui.press(p)

# pyautogui.hotkey('ctrl','shift','esc')
# >>> pyautogui.keyDown('ctrl')
# >>> pyautogui.keyDown('shift')
# >>> pyautogui.keyDown('esc')
# >>> pyautogui.keyUp('esc')
# >>> pyautogui.keyUp('shift')
# >>> pyautogui.keyUp('ctrl')

# pyautogui.keyDown('alt')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
#
# pyautogui.keyUp('alt')
# pyautogui.alert(text='a', title='b',button='OK')

# pyautogui.confirm(text='ss', title='aa', buttons=['OK', 'Cancel'])

#
# t = datetime.datetime.now().strftime("%Y-%M-%d %H-%M-%S")
# print(t)
# im = pyautogui.screenshot('{}.png'.format(t))
# pyautogui.moveTo(1652,359)

# pyautogui.moveTo(1677,179)

# button7location = pyautogui.locateOnScreen('calc7key.png')
# button7Center= pyautogui.center(button7location)
# print(button7Center)
#
# pyautogui.moveTo('calc7key.png')# shortcut version
try:
    # pyautogui.leftClick('calc7key.png')
    # pyautogui.leftClick('youtube.png')
    # pyautogui.leftClick('seoulnews.png')
    pyautogui.leftClick('naver.png')
except TypeError:
    print("Image not found")

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

# pyautogui.press('win')
# time.sleep(0.1)
# pyautogui.write('chrome')
# time.sleep(0.1)
# pyautogui.press('enter')
# time.sleep(0.1)
# pyautogui.write('naver.com')
# time.sleep(0.1)
# pyautogui.press('enter')