import math
import random as rd

def make_data() -> list:
    arr = []
    for i in range(0, 500):
        arr.append(rd.randint(1, 100))
    return arr

def main():
    arr = make_data()
    print(arr)
    print(len(arr))


if __name__ == "__main__":
    main()