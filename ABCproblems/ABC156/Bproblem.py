def Base_10_to_n(X, n): #さいとからぱくった
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

def main():
    N, K = map(int, input().split())
    nsin = Base_10_to_n(N, K)
    print(len(nsin))

if __name__ == '__main__':
    main()