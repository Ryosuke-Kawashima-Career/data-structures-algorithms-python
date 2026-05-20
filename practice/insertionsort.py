def insertionsort(arr):
    """
    Sorts the array using insertion sort algorithm
    """
    for right in range(1, len(arr)):
        key = arr[right]
        left = right - 1
        # Gradually shift
        while left >= 0 and arr[left] > key:
            arr[left + 1] = arr[left]
            left -= 1
        arr[left + 1] = key
    print(f"arr: {arr}\n")
        

def main():
    arr = [2, 1, 5, 7, 2, 0, 5]
    insertionsort(arr)

if __name__ == "__main__":
    main()
