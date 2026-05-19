def solve():
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements, key='transaction_amount')
    print(elements)

def bubble_sort(elements: list, key: str):
    n = len(elements)
    for i in range(n):
        for j in range(n-i-1):
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    print("elements has been sorted in acending order as per the key " + key)

def main():
    solve()

if __name__ == "__main__":
    main()