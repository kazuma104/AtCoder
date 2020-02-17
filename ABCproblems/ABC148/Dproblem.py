N = int(input())
a = list(map(int, input().split()))

count = 1
for i in range(N):
    if count == a[i]:
        count += 1

if (N-(count-1)) == N: print("-1")
else: print(N-(count-1))

