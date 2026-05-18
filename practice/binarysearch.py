def solution():
    numbers = [1,4,6,9,10,5,7]
    numbers.sort()
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    numbers.sort()
    index_l = lower_bound(numbers, number_to_find)
    index_r = upper_bound(numbers, number_to_find)
    print(f"First occurence : {index_l}")
    print(f"Last occurence : {index_r}")

def lower_bound(numbers, number_to_find):
    n = len(numbers)
    left = -1
    right = n
    while (right - left) > 1:
        mid = (left + right) // 2
        if numbers[mid] < number_to_find:
            left = mid
        else:
            right = mid
    return right

def upper_bound(numbers, number_to_find):
    n = len(numbers)
    left = -1
    right = n
    while (right - left) > 1:
        mid = (left + right) // 2
        if numbers[mid] <= number_to_find:
            left = mid
        else:
            right = mid
    return left

def binary_search_recursive(numbers, number_to_find, left, right) -> int:
    # Boundary Conditions
    if left > right:
        return -1
    mid = (left + right) // 2
    if mid < 0 or mid >= len(numbers):
        return -1
    if numbers[mid] == number_to_find:
        return mid
    
    if numbers[mid] < number_to_find:
        return binary_search_recursive(numbers, number_to_find, mid + 1, right)
    else:
        return binary_search_recursive(numbers, number_to_find, left, mid - 1)
    

if __name__ == '__main__':
    solution()
