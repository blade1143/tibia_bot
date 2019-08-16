from v3 import *


'''
version for 2 clients
Point(x=467, y=16) left

Point(x=1463, y=14) right
'''

def main():
    j = 0
    time.sleep(5)
    pyautogui.FAILSAFE = False
    while True:

        if j % 2 == 0:
            'right'
            move_mouse_cursor((1463, 16))
            time.sleep(1)
            print(time.asctime())
            key_bind('ESC')
            key_bind('F11')
            time.sleep(1)

            template_right = area([1253, 481, 1628, 622])
            any_screen = image_search_area('window_of_me.png', template_right)

            if any_screen != [-1, -1]:
                try:
                    screen_right = area([1252, 496, 1341, 510])
                    corr_answ = find_equation(screen_right)
                    corr_answ_value = eval(corr_answ)
                except:
                    key_bind('ESC')
                    continue

                try:
                    win, mou = window_right(), mouse_right()
                    final_answer = recognition(corr_answ_value, win, mou)
                    if final_answer == None:
                        key_bind('ESC')
                        continue
                except:
                    key_bind('ESC')
                    continue

        else:
            'left'
            move_mouse_cursor((467, 16))
            print('left')
            time.sleep(1)
            print(time.asctime())
            key_bind('ESC')
            key_bind('F11')
            time.sleep(1)

            template_left = area([293, 482, 666, 623])
            any_screen = image_search_area('window_of_me.png', template_left)

            if any_screen != [-1, -1]:

                try:

                    screen_left = area([292, 496, 379, 510])
                    corr_answ = find_equation(screen_left)
                    print(corr_answ)
                    corr_answ_value = eval(corr_answ)
                except:
                    key_bind('ESC')
                    continue

                try:
                    win, mou = window_left(), mouse_left()
                    final_answer = recognition(corr_answ_value, win, mou)
                    if final_answer == None:
                        key_bind('ESC')
                        continue
                except:
                    key_bind('ESC')
                    continue


        j += 1


if __name__ == "__main__":
    main()