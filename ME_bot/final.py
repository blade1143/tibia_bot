from main_functions import *
from basic_functions import *

'''
to install pytesseract u have to check this link below
https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
'''


def final_main():
    time.sleep(2)
    coo_tibia = [(470, 16), (1476, 16)]
    b = 2280
    # key_bind('F1')
    # key_bind('F2')

    while True:
        '''
        if u want to be sure ur tibia won't be in the background
        1) hash final_main()
        2) unhash check_pos()
        3) run a file
        4) check ur top tibia bar position
        5) close the program
        6) unhash final, hash check
        7) unhash move_mouse_cursor and time.sleep(1)
        8) write coordinates from console into X and Y
        9) run ur file
        '''
        # move_mouse_cursor((x, y))
        # time.sleep(1)
        '''
        u can replace F11, its !ME hotkey, F1 - F12
        '''
        key_bind('F11')
        main()

        '''
        # when u dont want to use shit below \/
        '''
        # a = time.clock()
        # if a > b:
        #     key_bind('F1')
        #     key_bind('F2')
        #     b += 2280


if __name__ == "__main__":
    final_main()
    # check_pos()
