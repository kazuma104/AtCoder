import collections
import math

def combinations_count2(n):
    return n*(n-1) // 2

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
#print(c)

d = {}
csum = 0
for i,j in c.items():
    if j == 1:
        d[i] = 0
        csum += 0
    else:
        d[i] =  combinations_count2(j)
        csum += d[i]

#print(c)
#print(d)
#print(csum)

#print(A)
for i in A:
    #print(c[i], i)
    if c[i] == 1:
        print(csum)
    elif c[i] == 2:
        print(csum-1)
    else:
        print(csum - combinations_count2(c[i]) + combinations_count2(c[i]-1))
