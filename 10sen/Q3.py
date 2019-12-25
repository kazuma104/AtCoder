N = int(input())
A = list(map(int, input().split()))

div = float("inf")
for i in range(N):
    count = 0
    while True:
        if A[i] % 2 == 0:
            A[i] /= 2
            count += 1
        else: break
    if div > count:
        div = count
print(div)


