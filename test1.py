import random
import numpy as np


def gen(n, prec, prec2):
    iter = 0
    iter_2 = 0
    for i in range(n):
        x = random.random()
        if x <= prec:
            iter += 1
            if x <= prec2:
                iter_2 += 1
    return iter, iter_2



lx, ly = [], []
for i in range(100):
    x, y = gen(1000, 0.13, 0.1)
    lx.append(x)
    ly.append(y)

# print(np.mean(lx), np.mean(ly))


def simul():
    z = 7
    j = 0
    jj = 0
    d = 0
    while j <= z and jj <= z:
        x = random.random()
        if x <= 0.5:
            j += 1
            jj = 0
        else:
            jj += 1
            j = 0
        d += 1


    return d

liss = []

# for i in range(10000):
# 	liss.append(simul())
# print(max(liss), min(liss))
# print('mean', np.mean(liss),
# 	  'median', np.median(liss),
# 	  'standard deviation', np.std(liss))
#
# plt.hist(liss, bins='auto')  # arguments are passed to np.histogram
# plt.title("Histogram with 'auto' bins")
# plt.show()
