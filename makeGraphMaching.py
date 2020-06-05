import numpy as np


def makeM(x1, y1, x2, y2):
    scale_2d = 0.1

    p1 = np.array([x1, y1]).T
    np1 = len(x1)
    e1 = np.ones((np1, np1))
    l1x, l1y = np.where(e1)
    g1 = p1[l1x, :] - p1[l1y, :]
    g1 = (g1[:, 0] ** 2 + g1[:, 1] ** 2) ** 0.5
    g1 = g1.reshape(np1, np1)

    p2 = np.array([x2, y2]).T
    np2 = len(x2)
    e2 = np.ones((np2, np2))
    l1x, l1y = np.where(e2)
    g2 = p2[l1x, :] - p2[l1y, :]
    g2 = (g2[:, 0] ** 2 + g2[:, 1] ** 2) ** 0.5
    g2 = g2.reshape(np2, np2)

    M = np.tile(g1, (np2, np2)) - np.kron(g2, np.ones((np1, np1)))
    M = np.exp(-M ** 2 / scale_2d)

    M-=np.diag(np.diag(M))#对角线置为0

    return M
