from fixed1 import *


def final_main():
    coo_tibia = [(470, 16), (1476, 16)]
    time.sleep(2)
    b = 2280
    # key_bind('F1')
    # key_bind('F2')
    print('glowna funkcja')
    while True:
        print('wchodzi do while')
        time.sleep(1)
        main()
        '''
        # when u dont want to use shit below \/
        '''
        a = time.clock()
        if a > b:
            key_bind('F1')
            key_bind('F2')
            b += 2280


if __name__ == "__main__":
    final_main()