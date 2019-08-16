import cv2
import time
import numpy as np
import pyautogui
from PIL import ImageEnhance, Image, ImageOps
import pytesseract
from v1 import area, check_pos, move_mouse_cursor, key_bind


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

'''
answer 1 area([777, 510, 816, 525])
answer 2 area([777, 525, 816, 540])
answer 3 area([777, 540, 816, 555])
answer 4 area([777, 553, 816, 567])
answer 5 area([777, 567, 816, 582])
'''


def find_equation(area_of_box):
    im = ImageOps.invert(area_of_box)
    im = ImageEnhance.Brightness(im)
    im = im.enhance(1)
    # im.show()
    text = pytesseract.image_to_string(im, lang='eng',
                                       config='--psm 10 --oem 3 -c tessedit_char_whitelist=-+0123456789')

    return text
# time.sleep(2)
# screenshot = area([770, 490, 857, 510])
# print(find_equation(screenshot))
# check_pos()


def window_mid():
    x1, y1, x2, y2, xyz = 779, 510, 816, 524, 14 #srodek
    mid_window = [[x1, y1, x2, y1 + xyz],
                  [x1, y1 + xyz, x2, y1 + (2 * xyz)],
                  [x1, y1 + (2 * xyz), x2, y1 + (3 * xyz)],
                  [x1, y1 + (3 * xyz), x2, y1 + (4 * xyz)],
                  [x1, y1 + (4 * xyz), x2, y1 + (5 * xyz)]]

    return mid_window


def mouse_mid():
    mouse = [(806, 515),
             (806, 530),
             (806, 545),
             (806, 560),
             (806, 575)]

    return mouse


def answer(area):
    im = ImageOps.invert(area)
    im = ImageEnhance.Brightness(im)
    im = im.enhance(1)
    # im.show()
    text = pytesseract.image_to_string(im, lang='eng',
                                       config='--psm 10 --oem 3 -c tessedit_char_whitelist=-+0123456789')

    return text
# for i in range(5):
# check_pos()


def recognition(value_of_equation, window, mouse):
    cooradinate_list = []

    for i in range(5):
        x = area(window[i])
        potential_answ = answer(x)

        potential_answ_value = int(potential_answ)

        cooradinate_list.append((window[i], mouse[i], potential_answ_value))

    value_list = [i[2] for i in cooradinate_list]
    set_value_list = set(value_list)

    if len(value_list) != len(set_value_list):
        return None

    if len(cooradinate_list) != 5:
        return None

    for i in range(5):

        if value_of_equation == cooradinate_list[i][2]:
            move_mouse_cursor(cooradinate_list[i][1])
            time.sleep(1)
            key_bind('ENTER')

    return value_of_equation


def image_search_area(template, image_life, precision=0.6, im=None):
    if im is None:
        im = image_life

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

