from collections import deque

N, K = map(int, input().split())

A = list(map(int, input().split()))
d = deque([A[0]])
telepote = A[0]
for i in range(K):
    d.append(A[telepote-1])
    if d.count(A[telepote-1]) >= 2:
        break
    telepote = A[telepote-1]


if len(d)>=K:
    print(d[K])
else:
    K -= len(d)-1
    a = d.pop()
    print(K)
    K = K%len(d)
    print(K)
    print(d[K-1])

print(d)