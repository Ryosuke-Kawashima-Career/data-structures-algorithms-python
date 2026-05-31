from typing import List, Tuple
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enque(self, val: str) -> None:
        self.buffer.appendleft(val)
    def deque(self) -> str:
        return self.buffer.pop()
    def is_empty(self) -> bool:
        return len(self.buffer) == 0
    def size(self) -> int:
        return len(self.buffer)
    def print(self) -> None:
        print(list(reversed(self.buffer)))
    def front(self) -> str:
        return self.buffer[-1]
    def append(self, val: int) -> None:
        if len(self.buffer) == 0:
            self.enque(str(val))
            return
        if len(self.buffer) == 1:
            self.enque("10")
            return
        if val % 2 == 0:
            val_bin = self.buffer[1] + "0"
            self.enque(val_bin)
        else:
            val_bin = self.buffer[1] + "1"
            self.enque(val_bin)



def main():
    binary_seq = Queue()
    for num in range(1, 11):
        binary_seq.append(num)
    binary_seq.print()

if __name__ == "__main__":
    main()
