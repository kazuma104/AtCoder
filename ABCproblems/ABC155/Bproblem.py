N = int(input())
A = list(map(int, input().split()))

flag = 1
for i in range(N):
    if(A[i] % 2 == 0):
        if(A[i] % 3 != 0 and A[i] % 5 != 0):
            flag = 0

if(flag == 0):
    print("DENIED")
else:
    print("APPROVED")