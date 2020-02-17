H = int(input())

for i in range(100000000): #とりあえず大きい数字
    if(2**i<=H and H<2**(i+1)):
        print(2**(i+1)-1)
        break
