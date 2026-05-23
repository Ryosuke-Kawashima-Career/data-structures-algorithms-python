from typing import Dict, List
def selectionsort(arr: List[Dict[str, str]], sort_keys: List[str] = ['First Name', 'Last Name']):
    """Sorts an array of people's names"""
    length = len(arr)
    for left in range(length):
        minimum = arr[left]
        index_minimum = left
        for right in range(left + 1, length):
            if arr[right][sort_keys[0]] < minimum[sort_keys[0]]:
                minimum = arr[right]
                index_minimum = right
            elif arr[right][sort_keys[0]] == minimum[sort_keys[0]]:
                if arr[right][sort_keys[1]] < minimum[sort_keys[1]]:
                    minimum = arr[right]
                    index_minimum = right
        if index_minimum != left:
            arr[left], arr[index_minimum] = arr[index_minimum], arr[left]
    print(arr)

def multi_key_selectionsort(arr: List[Dict[str, str]], sort_keys: List[str]):
    length = len(arr)
    # Reversed sort keys
    for sort_by in sort_keys[-1::-1]:
        for left in range(length):
            minimum = arr[left]
            index_minimum = left
            for right in range(left + 1, length):
                if arr[right][sort_by] < minimum[sort_by]:
                    minimum = arr[right]
                    index_minimum = right
            
            if index_minimum != left:
                arr[left], arr[index_minimum] = arr[index_minimum], arr[left]
    print(arr)


def main():
    names = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    multi_key_selectionsort(names, ['First Name', 'Last Name'])

if __name__ == "__main__":
    main()
