import numpy as np

N, M = map(int, input().split())
H = list(map(int, input().split()))

flag = np.full(N, True)
for i in range(M):
    A, B = map(int, input().split())
    if H[A-1] >= H[B-1]:
        flag[B-1] = False
    if H[B-1] >= H[A-1]:
        flag[A-1] = False

print(np.count_nonzero(flag))
     
