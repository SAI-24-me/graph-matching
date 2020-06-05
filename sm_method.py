import numpy as np


def sm_mehod(n, m, W):
    M=np.linalg.eig(W)[1][0,:]
    return abs(M.reshape(n,m))
