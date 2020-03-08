A, B = map(int, input().split())

#print((25*0.1)//1 == 2)
flag = 1
for i in range(1,100000):
    if (i*0.08)//1==A and (i*0.1)//1==B:
        flag = 0
        print(i)
        break

if flag:
    print("-1")