from fixed1 import *


def final_main():
    coo_tibia = [(470, 16), (1476, 16)]
    time.sleep(2)
    b = 1740

    while True:
        time.sleep(1)
        main()
        '''
        # when u dont want to use shit below \/
        '''
        a = time.clock()
        if a > b:
            key_bind('F2')
            key_bind('F4')
            b += 1740


if __name__ == "__main__":
    final_main()