# https://atcoder.jp/contests/abc280/tasks/abc280_e
import numpy as np
import math
import collections
N, P = map(int, input().split())
p = 998244353
inv = pow(100, -1, p)
critical = P*inv % p
normal = (100-P)*inv % p
ex_val = collections.defaultdict(int)
for i in range(N):
    ex_val[i+1] = (critical*ex_val[i-1]+normal*ex_val[i]+1) % p
print(ex_val[N])
a = math.sin(60)
np.
