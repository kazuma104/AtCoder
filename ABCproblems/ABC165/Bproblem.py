X = int(input())
yen = 100
year = 10**18

for i in range(year):
    yen *= 1.01
    yen = int(yen)
    #print(yen)
    if X <= yen:
        break

print(i+1)