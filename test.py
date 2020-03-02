import time

def hairetu():
    s1 = [2, 3]*5
    s2 = [[2, 3] for _ in range(5)]
    s3 = [[2, 3]*5]

    print(s1,s2,s3)

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
