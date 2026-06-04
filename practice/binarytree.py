from typing import List, Optional, Tuple
from pydantic import BaseModel

class TreeNode(BaseModel):
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None
    
    def new(self, val: int) -> TreeNode:
        return TreeNode(val=val)
    
    def insert(self, val: int) -> None:
        """Insert a new value into the tree."""
        if val <= self.val:
            if self.left is None:
                self.left = TreeNode(val=val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val=val)
            else:
                self.right.insert(val)

    
    def find_min(self) -> TreeNode:
        """Find the minimum value node in the tree."""
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find_max(self) -> TreeNode:
        """Find the maximum value node in the tree."""
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def calculate_sum(self) -> int:
        """Calculate the sum of all values in the tree."""
        if self is None:
            return 0
        sum_result = self.val
        if self.left is not None:
            sum_result += self.left.calculate_sum()
        if self.right is not None:
            sum_result += self.right.calculate_sum()
        return sum_result
    
    def post_order_traversal(self, result: List[int]) -> List[int]:
        """Perform post-order traversal of the tree and store values in result."""
        if self.left is not None:
            self.left.post_order_traversal(result)
        if self.right is not None:
            self.right.post_order_traversal(result)
        if self is not None:
            result.append(self.val)
        return result
    
    def pre_order_traversal(self, result: List[int]) -> List[int]:
        """Perform pre-order traversal of the tree and store values in result."""
        if self is not None:
            result.append(self.val)
        if self.left is not None:
            self.left.pre_order_traversal(result)
        if self.right is not None:
            self.right.pre_order_traversal(result)
        return result
    
def main():
    root = TreeNode(val=10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(12)
    root.insert(18)

    print("Pre-order traversal:", root.pre_order_traversal([]))
    print("Post-order traversal:", root.post_order_traversal([]))
    print("Sum of all values:", root.calculate_sum())
    print("Minimum value:", root.find_min().val)
    print("Maximum value:", root.find_max().val)

if __name__ == "__main__":
    main()
