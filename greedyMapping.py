import numpy as np


def gm(W):
    xy = []

    maxx = np.where(W == np.max(W))[0][0]
    maxy = np.where(W == np.max(W))[1][0]
    while W[maxx][maxy] != 0:
        xy.append((maxx, maxy))
        W[:, maxy] = 0
        W[maxx, :] = 0
        maxx = np.where(W == np.max(W))[0][0]
        maxy = np.where(W == np.max(W))[1][0]
    return xy


if __name__ == '__main__':
    x, y = 4, 3
    ans = np.random.rand(x, y)
    print(ans)
    line = gm(ans)
    for i, j in line:
        print(i, j)
