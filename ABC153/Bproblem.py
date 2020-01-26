H, N = map(int, input().split())
A = list(map(int, input().split()))

kougeki = 0
for i in range(N):
    kougeki += A[i]

if(kougeki>=H):
    print("Yes")
else:
    print("No")