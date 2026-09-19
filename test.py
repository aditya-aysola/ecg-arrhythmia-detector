def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        current = arr[i]
        inner_index = i
        while inner_index > 0:
            if arr[inner_index - 1] > current:
                temp = arr[inner_index - 1]
                arr[inner_index - 1] = current
                arr[inner_index] = temp

            inner_index -= 1

def main():
    arr = [5, 3, 4, 1, 2]
    insertion_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()