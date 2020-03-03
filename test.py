import time

def hairetu():
    s1 = [2, 3]*5
    s2 = [input().split() for _ in range(5)]
    s3 = []
    s4 = []
    for _ in range(5):
        s3.append([2, 3])
        s4.extend([2, 3])
    s5 = [i for i in input().split()]
    print(s1,s2,s3,s4,s5,sep="\n")

def time_module():
    t1 = time.time()

    for _ in range(1):
        s1 = [input() for _ in range(3)]

    t2 = time.time()

    for _ in range(10):
        s2 = [[i for i in [2, 3]] for _ in range(10)]

    print(s1,s2)
    t3 = time.time()

    print(f"処理1:{t2-t1}")
    print(f"処理2:{t3-t2}")

def main():
    #time_module()
    hairetu()


if __name__ == "__main__":
    main()
