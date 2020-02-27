N = int(input())
P = list(map(int, input().split()))

Pmin = float("inf")
count = 0
for i in P:
    if i < Pmin:
        Pmin = i
        count += 1

print(count)