from v2 import *

'''
version for 1 client
'''
def main():
    time.sleep(5)
    pyautogui.FAILSAFE = False
    while True:
        move_mouse_cursor((1463, 16))
        time.sleep(1)
        print(time.asctime())
        key_bind('ESC')
        key_bind('F11')
        time.sleep(1)

        any_screen = image_search_area('window_of_me.png', area([772, 478, 1143, 617]))

        if any_screen != [-1, -1]:
            print('2')
            try:
                screenshot = area([770, 490, 857, 510])
                corr_answ = find_equation(screenshot)
                corr_answ_value = eval(corr_answ)
            except:
                key_bind('ESC')
                continue


            try:
                win, mou = window_mid(), mouse_mid()
                final_answer = recognition(corr_answ_value, win, mou)
                if final_answer == None:
                    key_bind('ESC')
                    continue
            except:
                key_bind('ESC')


if __name__ == "__main__":
    main()