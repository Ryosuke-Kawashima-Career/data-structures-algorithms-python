def quicksort(arr, low, high):
    """
    Sorts the array[low..high]
    """
    if low >= high or low < 0 or high > len(arr):
        return
    pivot = partition(arr, low, high)
    print(f"arr: {arr}, low: {low}, high: {high}, pivot: {pivot}\n")
    quicksort(arr, low, pivot)
    quicksort(arr, pivot + 1, high)
    
    

def partition(arr, low, high):
    """
    Partitions the array and return the index of the pivot element
    """
    pivot = arr[high - 1]
    # lower than pivot
    pivot_index = low
    # j searches for elements less than pivot
    for j in range(low, high):
        if arr[j] < pivot:
            arr[pivot_index], arr[j] = arr[j], arr[pivot_index]
            pivot_index += 1
    arr[pivot_index], arr[high - 1] = arr[high - 1], arr[pivot_index]
    return pivot_index


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
