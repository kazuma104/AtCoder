N, A, B = map(int, input().split())

sum = 0

for i in range(1,N+1):
    n = i
    dsum = 0 #digit sum (桁の和)
    while True:
        dsum += (n % 10)

        if n // 10 == 0: break
        else:
            n //= 10 
            continue
    if (A <= dsum) and (dsum <= B):
        sum += i
        
print(sum)

