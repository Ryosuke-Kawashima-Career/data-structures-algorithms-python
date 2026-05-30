import time
import threading
from typing import List, Tuple, Any
from collections import deque

def place_order(array: deque[str]) -> None:
    """Insert an order into the array"""
    orders_to_place = list(array)
    array.clear()
    for order in orders_to_place:
        print("Placing order for:", order)
        array.append(order)
        time.sleep(0.5)


def serve_order(array: deque[str]) -> None:
    """Pop an order from the array"""
    time.sleep(1.0)
    while True:
        if len(array) > 0:
            result = array.popleft()
            print("Now serving: ",result)
        else:
            break
        time.sleep(2.0)



def main():
    orders = deque(['pizza','samosa','pasta','biryani','burger'])
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order, args=(orders,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
