import time

j = 0
xd = 0
while True:
    time.sleep(2)
    print('pocz')

    if j % 2 == 0:
        print('xd1')
        if xd == 0:
            print('j1')
            try:
                x = int(input('int'))

            except:
                print('fail')
                continue

    else:
        print('j1')

        try:
            d = int(input('int drugi'))

        except:
            print('fail drugi')
            continue

    j += 1

