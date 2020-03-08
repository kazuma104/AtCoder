from collections import deque

S = input()
Q = int(input())
d = deque(S)
#print(d)

mod = 0 #反転が何回目か（先頭がどっちか）,偶数回の時0，奇数回の時1

for _ in range(Q):
    Query = input()
    if Query[0] == "1":
        mod = (1 + mod) % 2
    else:
        if Query[2] == "1":
            if mod == 0:
                d.appendleft(Query[4])
            else:
                d.append(Query[4])
        else:
            if mod == 0:
                d.append(Query[4])
            else:
                d.appendleft(Query[4])

S = ""
if mod==0: #反転されていたら，popする．
    for _ in range(len(d)):
        S += d.popleft()
else:
    for _ in range(len(d)):
        S += d.pop()
print(S)