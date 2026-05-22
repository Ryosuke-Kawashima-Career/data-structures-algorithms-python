from typing import List

def shellsort(arr: List[int]):
    """Sorts an array using the shell sort algorithm."""
    n = len(arr)
    gap = n // 2
    while gap > 0:
        indices_to_delete = []
        for right in range(gap, n):
            current = arr[right]
            left = right
            while left >= gap and arr[left - gap] > current:
                if arr[left - gap] == current:
                    indices_to_delete.append(right)
                # Move the larger element to the right
                arr[left] = arr[left -gap]
                left -= gap
            # Place the current element in its correct position
            arr[left] = current
        for index in sorted(indices_to_delete, reverse=True):
            del arr[index]
        gap //= 2
                
    print("Sorted array:", arr)

def main():
    arr = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    shellsort(arr)

if __name__ == "__main__":
    main()
