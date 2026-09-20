import math
import random as rd
import wfdb
import numpy as np

np.random.seed(42)
scores = np.random.randint(50, 101, size=(20, 4))

def main():
    print("hi")
    print(test_sum(3,1))
    for i in range(1, 5):
        print("testing")
    rows, cols = scores.shape
    print(f"Number of students: {rows}")
    print(f"Number of exams: {cols}")
    print(f"Overall average: {scores.mean(axis=1)}" )

    # highest score

def test_sum(a : int, b : int) -> int:
    return a + b

if __name__ == "__main__":
    main()