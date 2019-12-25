#10の倍数は必ず5を素因数にもつ．
#1000なら少なくとも100個の5を素因数にもつ数がある．
#次に50の倍数は必ず2つの5を素因数にもつ
#なので10の倍数の時に判定できなかったもう一つの5を50で割ることで見つける．
#以降繰り返すと求まる．終了条件は割る数が元の数より大きくなったとき．

N = int(input())
count = 0
mul = 10

if (N % 2) == 0:
    while True:
        count += N // mul
        mul *= 5
        if mul > N: break
    print(count)
else:
    print(0)