N = int(input())
flag = 0

for i in range(1,50001):
  if int(i*1.08) == N:
    print(i)
    flag = 1
  elif (flag == 0) and (i == 50000):
    print(":(")
