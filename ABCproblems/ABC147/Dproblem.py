N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
xorsum = 0
for i in range(60):
  c1 = sum([1 for a in A if (a >> i) & 1]) #
  xorsum += (c1*(N-c1)*(1<<i))
  xorsum = xorsum%mod
print(xorsum%mod)
