H, N = map(int, input().split())

AB = []
ABdiv = []

for i in range(N):
    A, B = map(int, input().split())
    AB.append([A,B])
    ABdiv.append(A/B)

print(ABdiv[0], ABdiv[1], ABdiv[2])
sortAB = [sorted(ABdiv).index(s) for s in ABdiv]
print(sortAB)
print(max(zip(sortAB, range(len(sortAB)))))
#for _ in range(10000000):


