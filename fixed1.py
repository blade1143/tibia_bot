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


def image_recognition(area_of_box):
    im = ImageOps.invert(area_of_box)
    im = ImageEnhance.Brightness(im)
    im = im.enhance(1)
    x, y = im.size
    a = im.resize((x*2, y*2), resample=1)
    # a.show()
    text = pytesseract.image_to_string(a, lang='eng',
                                       config='--psm 10 --oem 3 -c tessedit_char_whitelist=-+0123456789')

    return text


def co_ordinates_mouse(x, y):
    a = 15
    mouse = [(x + 34, y + 37),
             (x + 34, y + 37 + a),
             (x + 34, y + 37 + 2*a),
             (x + 34, y + 37 + 3*a),
             (x + 34, y + 37 + 4*a)]

    return mouse


def co_ordinates_answers(a, b):
    # x1, y1, x2, y2, xyz = 777, 510, 816, 524, 14
    x1, y1 = a + 6, b + 32
    x2, y2 = x1 + 39, 0
    xyz = 14
    mid_window = [[x1, y1, x2, y1 + xyz],
                  [x1, y1 + xyz, x2, y1 + (2 * xyz)],
                  [x1, y1 + (2 * xyz), x2, y1 + (3 * xyz)],
                  [x1, y1 + (3 * xyz), x2, y1 + (4 * xyz)],
                  [x1, y1 + (4 * xyz), x2, y1 + (5 * xyz)]]

    return mid_window


def co_ordinates_equation(a, b):
    x1, y1 = a - 2, b + 12
    x2, y2 = x1 + 90, y1 + 20

    return x1, y1, x2, y2


def template_recognition(name_of_screen):
    window = pyautogui.screenshot()
    x, y = window.size
    x_y_found_equation = image_search_area(name_of_screen, area([0, 0, x, y]))

    return x_y_found_equation


def correct_answer_chooser(answers_coordinates, mouse_coordinates):
    list_of_answers = []

    for i in range(5):
        try:
            answers_window = image_recognition(area(answers_coordinates[i]))
            int_answer = int(answers_window)
            # print(int_answer) # print each answer
            list_of_answers.append([int_answer, answers_coordinates[i] ,mouse_coordinates[i]])
        except:
            return False

    list_of_anwers2 = [i[0] for i in list_of_answers]
    set_of_answers = set(list_of_anwers2)

    if len(list_of_answers) != len(set_of_answers):
        raise ValueError

    if len(list_of_answers) != 5:
        raise ValueError

    return list_of_answers


# def main():
#     # while True:
#     #     time.sleep(2)
#     key_bind('F11')
#     x_axis, y_axis = template_recognition('window_of_me.png')
#     # print('templatka', x_axis, y_axis)
#     if [x_axis, y_axis] != [-1, -1]:
#         try:
#             x1, y1, x2, y2 = co_ordinates_equation(x_axis, y_axis)
#             # print('rownanie', x1, y1, x2, y2)
#             mouse_xy = co_ordinates_mouse(x_axis, y_axis)
#             # print('mysz', mouse_xy)
#             # move_mouse_cursor((x_axis, y_axis))
#             answers_xy = co_ordinates_answers(x_axis, y_axis)
#             # print('odpowiedzi', answers_xy)
#             equation = image_recognition(area([x1, y1, x2, y2]))
#             # print('str rownanie',equation)
#             eval_equation = eval(equation)
#             # print('int rownanie', eval_equation)
#             back = False
#         except:
#             back = True
#             key_bind('ESC')
#             # continue
#         if back == True:
#             key_bind('ESC')
#         else:
#             list_of_answers = correct_answer_chooser(answers_xy, mouse_xy)
#
#             if list_of_answers == False:
#                 key_bind('ESC')
#             else:
#                 for answer in list_of_answers:
#                     if answer[0] == eval_equation:
#                         move_mouse_cursor((answer[2]))
#                         key_bind('ENTER')
#                         break
#                 key_bind('ESC')


def main():
    # while True:
    #     time.sleep(2)
    key_bind('F11')
    x_axis, y_axis = template_recognition('window_of_me.png')
    # print('templatka', x_axis, y_axis)
    if [x_axis, y_axis] != [-1, -1]:
        try:
            x1, y1, x2, y2 = co_ordinates_equation(x_axis, y_axis)
            mouse_xy = co_ordinates_mouse(x_axis, y_axis)

            answers_xy = co_ordinates_answers(x_axis, y_axis)

            equation = image_recognition(area([x1, y1, x2, y2]))

            eval_equation = eval(equation)

            list_of_answers = correct_answer_chooser(answers_xy, mouse_xy)

            for answer in list_of_answers:
                if answer[0] == eval_equation:
                    move_mouse_cursor((answer[2]))
                    key_bind('ENTER')
                    return True

        except:
            key_bind('ESC')
