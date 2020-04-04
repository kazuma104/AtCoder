N, M = map(int, input().split())
A = list(map(int, input().split()))

Asum = sum(A)
hyou = Asum * (1/(4*M))
count = 0
for i in A:
    if i >= hyou:
     count += 1

if count >= M:
    print("Yes")
else:
    print("No")