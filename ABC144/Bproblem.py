N = int(input())

flag = True

for i in range(1,10):
    for j in range(1,10):
        #print(i, j)
        if i * j == N:
            print("Yes")
            flag = False
    if not(flag):
        break

if flag:
    print("No")
