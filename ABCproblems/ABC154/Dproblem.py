N, K = map(int,input().split())
p = list(map(int,input().split()))

S = 0
maxsum = 0
for i in range(K):
    S += (p[i]+1)/2

for i in range(K,N):
    if(maxsum < S):
        maxsum = S
    S = S + (p[i]+1)/2 - (p[i-K]+1)/2

if(maxsum < S): #最後のみfor文からはずれるので．
    maxsum = S

print(maxsum)

