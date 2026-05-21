def mergesort(arr, key):
    """Sorts an array of dictionaries based on a specified key using the merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid], key)
    right_half = mergesort(arr[mid:], key)
    return merge(left_half, right_half, key)

def merge(left_arr, right_arr, key):
    merged_arr = []
    index_left = index_right = 0
    while index_left < len(left_arr) and index_right < len(right_arr):
        if left_arr[index_left][key] < right_arr[index_right][key]:
            merged_arr.append(left_arr[index_left])
            index_left += 1
        else:
            merged_arr.append(right_arr[index_right])
            index_right += 1
    while index_left < len(left_arr):
        merged_arr.append(left_arr[index_left])
        index_left += 1
    while index_right < len(right_arr):
        merged_arr.append(right_arr[index_right])
        index_right += 1
    return merged_arr

def main():
    elements =  [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    print(mergesort(elements, 'age'))

if __name__ == "__main__":
    main()