from itertools import permutations 
N = int(input())

point = [] 
for i in range(N):
    x,y = map(int, input().split())
    point.append([x,y])


perm = list(range(N))

count = 0
distsum = 0
for i in permutations(perm):
    for j, k in zip(i, i[1:]):
        x1, y1 = point[j]
        x2, y2 = point[k]
        distsum += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    count += 1

print(distsum / count)