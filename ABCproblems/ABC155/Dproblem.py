N, K= map(int, input().split())
A = list(map(int, input().split()))
posi = []
zero = []
nega = []
for i in A:
    if i == 0:
        zero.append(i) 
    elif i == abs(i):
        posi.append(i)
    else:
        nega.append(i)

sign = len(nega), len(zero), len(posi) # 掛けて負，0，正になるもの
sign_pair = [0]*3
sign_pair[0] = sign[0]*sign[2]
sign_pair[1] = (sign[0]+sign[2])*sign[1] + (sign[1]*(sign[1]-1))//2
# sign_pair[2] = (sign[0]*(sign[0]-1))//2 + (sign[2]*(sign[2]-1))//2

#print(sign_pair)

seki = []
if K <= sign_pair[0]:
    for i in nega:
        for j in posi:
            seki.append(i*j)
    seki.sort()
    print(seki[K-1])

elif sign_pair[0]+sign_pair[1] < K:
    for i in range(sign[0]):
        for j in range(i+1, sign[0]):
            seki.append(nega[i]*nega[j])
    for i in range(sign[2]):
        for j in range(i+1, sign[2]):
            seki.append(posi[i]*posi[j])
    seki.sort()
    print(seki[K-sign_pair[0]-sign_pair[1]-1])

else:
    print("0")

print(seki)