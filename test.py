def main():
    print("hi")
    print(test_sum(3,1))
    for i in range(1, 5):
        print("testing")


def test_sum(a : int, b : int) -> int:
    return a + b

if __name__ == "__main__":
    main()