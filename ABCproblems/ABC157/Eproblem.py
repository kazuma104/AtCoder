import collections

N = int(input())
S = input()
Q = int(input())
query = []
for _ in range(Q):
    query.append(list(input().split()))

#print(len(collections.Counter(S[2:6]).most_common()))

#print(query)
for q in query:
    if q[0] == "1":
        S = S[:(int(q[1])-1)]+q[2]+S[int(q[1]):]
    else:
        print(len(collections.Counter(S[int(q[1])-1:int(q[2])]).most_common()))
#print(S)
        

