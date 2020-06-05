import numpy as np


def ga_mehod(n, m, W):
    B0 = 0.5
    BF = 10
    BR = 1.075
    I0 = 4
    I1 = 30
    E = 0.5
    M = np.random.rand(W.shape[0]).reshape(W.shape[0], 1)
    B = B0
    M0 = M
    while B < BF:
        FLAG1 = True
        iter1 = 0
        while iter1 <= I0 and FLAG1:
            iter1 += 1
            M = M0.copy()
            Q = np.dot(W, M)
            M0 = np.exp(B * Q)
            iter2 = 0
            FLAG2 = True
            while iter2 <= I1 and FLAG2:
                M0 = M0.reshape(n, m)
                iter2 += 1
                M_BEFORE = M0.copy()
                M0 = M0 / np.tile(M0.sum(axis=1), (m, 1)).T
                M0 = M0 / np.tile(M0.sum(axis=0), (n, 1))
                FLAG2 = True if np.sum(abs(M_BEFORE - M0)) > E/10 else False
            M0 = M0.reshape(n * m, 1)
            FLAG1 = True if np.sum(abs(M - M0)) > E else False
        B = BR * B
    M = M.reshape(n, m)
    return M

