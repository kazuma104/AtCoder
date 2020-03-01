m = int(input())

if 100>m:
    print(format(0,'02'))    
elif 5000>=m and m>=100:
    print(format((m*10)//1000,'02')) #二桁ゼロ埋め
elif 30000>=m and m>=6000:
    print((m//1000)+50)
elif 70000>=m and m>= 35000:
    print(((m//1000)-30)//5+80)
else:
    print(89)
