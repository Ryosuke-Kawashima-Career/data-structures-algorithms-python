from typing import List, Optional, Tuple
from pydantic import BaseModel

class TreeNode(BaseModel):
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None
    
    def new(self, val: int) -> TreeNode:
        return TreeNode(val=val)
    
    def find_min(self) -> TreeNode:
        """Find the minimum value node in the tree."""
        pass

    def find_max(self) -> TreeNode:
        """Find the maximum value node in the tree."""
    
    def calculate_sum(self) -> int:
        """Calculate the sum of all values in the tree."""
    
    def post_order_traversal(self, result: List[int]) -> None:
        """Perform post-order traversal of the tree and store values in result."""
    
    def pre_order_traversal(self, result: List[int]) -> None:
        """Perform pre-order traversal of the tree and store values in result."""
        