from collections import deque

N = int(input())
A = list(map(int, input().split()))

A.sort()
Aque = deque(A)
out = deque()
out.append(Aque.popleft())

if out[0] != 1:
    for i in range(N-1):
        yaku = Aque.popleft()
        flag = 1
        for j in out:
            if yaku % j == 0:
                flag = 0
                break
        if flag:
            out.append(yaku)

    ans = len(out)
    if ans == 1:
        print("0")
    else:
        print(ans)
else:
    print("1")