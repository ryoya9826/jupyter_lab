import pandas as pd
import math
import numpy as np
from numpy import linalg as LA

u = np.array([3, 4])
v = np.array([-4, 3])


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)


def angle(p1, p2):
    u = np.array(p1)
    v = np.array(p2)
    i = np.inner(u, v)
    n = LA.norm(u) * LA.norm(v)
    c = i/n
    return np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))


S = [input() for _ in range(9)]

for i in range(9):
    S[i] = [S[i][j] for j in range(9)]

l = []
for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            l.append([i, j])


def equal_list(x):
    D = []
    for y in l:
        D.append([y, dist(x, y)])
    return D


ans_D = []
for x in l:
    for s in l:
        for t in l:
            if dist(x, s) == dist(x, t):
                u = [s[0]-x[0], s[1]-x[1]]
                v = [t[0]-x[0], t[1]-x[1]]
                if angle(u, v) == 90:
                    for y in l:
                        u = [s[0]-y[0], s[1]-y[1]]
                        v = [t[0]-y[0], t[1]-y[1]]
                        if y != x and dist(y, s) == dist(x, s) and angle(u, v) == 90:
                            ans_D.append([x, s, t, y])

for i in range(len(ans_D)):
    ans_D[i].sort()
    ans_D[i] = [tuple(x) for x in ans_D[i]]
A = set(map(tuple, ans_D))
print(len(A))
pd.HDFStore
np.
