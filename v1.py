import time
import pyautogui
from PIL import Image


def key_bind(specif_key):
    return pyautogui.hotkey(specif_key)

'''
position to !me window
</\ Point(x=772, y=478)
>/\ Point(x=1143, y=481)
<\/ Point(x=773, y=617)
>\/ Point(x=1145, y=617)
'''

def move_mouse_cursor(x):
    pyautogui.moveTo(x)
    # pyautogui.doubleClick()
    pyautogui.click()


def check_pos():
    x = 0
    while True:
        print(pyautogui.position())
        if x == 1:
            continue
        time.sleep(1)
        x = input(': ')
'''
unhash to check ur window + answers postion
'''
# check_pos()

def area(pos):
    x1 = pos[0]
    y2 = pos[1]
    width = pos[2] - x1
    height = pos[3] - y2

    return pyautogui.screenshot(region=(x1, y2, width, height))


def area_save_file(pos, name):
    x1 = pos[0]
    y2 = pos[1]
    width = pos[2] - x1
    height = pos[3] - y2

    return pyautogui.screenshot(name, region=(x1, y2, width, height))

# area_save_file([772, 478, 1143, 617], 'window_of_me.png')
# pyautogui.screenshot('game_img.png')
