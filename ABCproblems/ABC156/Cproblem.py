def main():
    N =int(input())
    X = list(map(int, input().split()))

    minimum = float("inf")
    for i in range(1,101):
        hpmin = 0
        for j in X:
            hpmin += (i-j)**2
        minimum = min(hpmin, minimum)
    print(minimum)
    
if __name__ == '__main__':
    main()