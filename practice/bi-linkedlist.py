from typing import Any, List, Optional

class Node:
    def __init__(self, data: Any = None, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.data: any = data
        self.next: Optional['Node'] = next
        self.prev: Optional['Node'] = prev

class BiLinkedList:
    def __init__(self):
        self.head: Optional[Node] = Node()
        self.tail: Optional[Node] = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size: int = 0
    
    def __iter__(self):
        """Turns the linked list into an iterable for 'for' loops.
        
        Yields: 
            Any: The data of the current node.
        """
        curr = self.head.next
        while curr.data is not None and curr is not self.tail:
            yield curr.data
            curr = curr.next

    def insert_at_end(self, data: Any) -> None:
        new_node = Node(data=data, next=self.tail, prev=self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    
    def insert_values(self, values: List[Any]) -> None:
        for value in values:
            self.insert_at_end(value)
    
    def insert_after_value(self, data_after: Any, data_to_insert: Any) -> None:
        new_node = Node(data=data_to_insert, next=None, prev=None)
        curr = self.head.next
        while curr.data is not None and curr is not self.tail:
            if curr.data == data_after:
                new_node.prev = curr
                new_node.next = curr.next
                curr.next.prev = new_node
                curr.next = new_node
                self.size += 1
                return
            curr = curr.next
        print("Value not found in the list.")
    
    def remove_by_value(self, data_to_remove: Any) -> None:
        curr = self.head.next
        while curr.data is not None and curr is not self.tail:
            if curr.data == data_to_remove:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                self.size -= 1
                return
            curr = curr.next
        print("Value not found in the list.")
    
    def print_forward(self) -> None:
        curr = self.head.next
        while curr.data is not None and curr is not self.tail:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()
    
    def print_backward(self) -> None:
        curr = self.tail.prev
        while curr.data is not None and curr is not self.head:
            print(curr.data, end=" --> ")
            curr = curr.prev
        print()
    
def main():
    ll = BiLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_forward()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_forward()
    ll.remove_by_value("figs")
    ll.print_forward()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_forward()

if __name__ == "__main__":
    main()
