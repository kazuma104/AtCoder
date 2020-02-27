N = int(input())
c = [[0]*9 for _ in range(9)]
count = 0
for i in range(1,N+1):
    li = i//10**(len(str(i))-1) 
    ri = i%10
    if ri == 0:
        continue
    c[li-1][ri-1] += 1

for i in range(9):
    for j in range(9):
        count += c[i][j]*c[j][i]

print(count)