import collections

N = int(input())
A = list(map(int, input().split()))

#ren = [0]*(10**9+2*(10**5))

L = [0]*N
R = [0]*N

for i in range(N):
    L[i] = (i+1) + A[i]
    R[i] = (i+1) - A[i]

l = collections.Counter(L)
r = collections.Counter(R)

#print(l,r)
#print(l.items(),l.keys())

count = 0
for i in l.keys():
    for j in r.keys():
        #print(i,j)
        if i == j:
            count += l[i] * r[j]

print(count)
