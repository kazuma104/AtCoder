S = input()

N = len(S)
N1 = (N-1)//2
N2 = (N+3)//2
#print(N1,N2)
flag = 0

for i in range(N//2):
    #print(S[i], S[-(i+1)])
    if S[i] != S[-(i+1)]:
        flag = 1

for i in range(N1//2):
    #print(S[i], S[-(i+1+N1+1)])
    if S[i] != S[-(i+1+N1+1)]:
        flag = 1

for i in range(N1//2):
    #print(S[i+N2-1], S[-(i+1)])
    if S[i+N2-1] != S[-(i+1)]:
        flag = 1

if flag:
    print("No")
else:
    print("Yes")