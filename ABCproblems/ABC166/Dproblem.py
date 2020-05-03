def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
X = int(input())
soin = factorization(X)
small = soin[0][0]

for i in range(10**9):
    if i**5-(i-small)**5==X:
        print(i,i-small)
        break