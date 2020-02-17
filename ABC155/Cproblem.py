import collections
from operator import itemgetter

N = int(input())
S = []
for _ in range(N):
    S.append(input())

s = collections.Counter(S)
#print(list(s.items()))
ss = list(s.items())
#s2 = collections.OrderedDict(s)
maxint = s.most_common()[0][1]
s3 = sorted(ss, key=itemgetter(0))
s4 = sorted(s3, key=itemgetter(1), reverse=True)
#print(s3,s4,sep="\n")

count = 0
for i in range(N):
    if(s4[i][1] == maxint):
        print(s4[i][0])
        count += s4[i][1]
        if(N==count):
            break
    else:
        break

