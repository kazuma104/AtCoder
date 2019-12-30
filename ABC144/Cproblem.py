import math

N = int(input())

hoji = float("inf")
for i in range(1,int(math.sqrt(N))+1):
    if N%i == 0 and (i-1)+((N//i)-1) < hoji:
        hoji = (i-1)+((N//i)-1)

print(hoji)
