import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
A = list(map(int, input().split()))
z = collections.Counter()
y = []

for i in A:
    c = collections.Counter(prime_factorize(i))
    for j in c.keys():
        if j in z:
            #print(c[j], z[j])
            z += collections.Counter({j: max(0, c[j]-z[j])})
        else:
            z += c

print(z)
for i in A:
    c = collections.Counter(prime_factorize(i))
    z += c
    y += c.items()
    print(c, c.items())