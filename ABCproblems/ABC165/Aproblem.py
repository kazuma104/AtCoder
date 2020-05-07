K = int(input())
A, B = map(int, input().split())

flag = False
for i in range(1000):
    if A <= i*K and i*K <= B:
        flag = True

if flag:
    print("OK")
else:
    print("NG")