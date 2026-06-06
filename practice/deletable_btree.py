from typing import List, Optional
from pydantic import BaseModel
class BtreeNode(BaseModel):
    value: int
    left: Optional[BtreeNode] = None
    right: Optional[BtreeNode] = None

    def new(self, value: int) -> BtreeNode:
        return BtreeNode(value=value)
    
    def insert(self, value: int) -> None:
        current = self
        if value <= current.value:
            if current.left is None:
                current.left = BtreeNode(value=value)
            else:
                current.left.insert(value)
        else:
            if current.right is None:
                current.right = BtreeNode(value=value)
            else:
                current.right.insert(value)
    
    def find_min(self) -> BtreeNode:
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self) -> BtreeNode:
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def delete(self, value: int) -> Optional[BtreeNode]:
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
            else:
                return None
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
            else:
                return None
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                # Node to be deleted has two children
                max_node = self.right.find_max()
                self.value = max_node.value
                self.right = self.right.delete(max_node.value)
        return self
    def print(self, level=0) -> str:
        result = ""
        if self.right is not None:
            result += self.right.print(level + 1)
        result += " " * 4 * level + "-> " + str(self.value) + "\n"
        if self.left is not None:
            result += self.left.print(level + 1)
        return result
    
def main():
    root = BtreeNode(value=10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(12)
    root.insert(18)

    print("Before deletion:")
    root.print()

    root.delete(10)

    print("After deletion:")
    root.print()

if __name__ == "__main__":
    main()

