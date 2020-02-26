def main():
    N, R = map(int, input().split())
    if N < 10:
        N = 100 * (10 - N)
    else:
        N = 0
    print(N+R)

if __name__ == '__main__':
    main()