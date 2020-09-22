N = int(input())

count = 0
flag = 0
for i in range(N):
    D = list(map(int, input().split()))
    if D[0] == D[1]:
        count += 1
    else:
        count = 0
    if count == 3:
        flag = 1

if flag == 0:
    print("No")
else:
    print("Yes")
