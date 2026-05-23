from typing import Any, List, Optional

class Node:
    """A node in a singly linked list."""
    def __init__(self, data: Any = None, next: Optional['Node'] = None):
        self.data: Any = data
        self.next: Optional['Node'] = next

    def __repr__(self) -> str:
        return f"Node({self.data})"


class LinkedList:
    """A robust, type-hinted Singly Linked List with O(1) size and tail tracking."""
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0
    
    def __len__(self) -> int:
        """Returns the number of elements in the list in O(1) time."""
        return self.size

    def __iter__(self):
        """Allows direct iteration over node data, e.g., [x for x in ll]."""
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def insert_at_end(self, data: Any) -> None:
        """Inserts a new node at the end of the list in O(1) time."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_values(self, values: List[Any]) -> None:
        """Resets the list and populates it with a list of values."""
        self.head = None
        self.tail = None
        self.size = 0
        for value in values:
            self.insert_at_end(value)
        print("Insertion finished!...")

    def insert_after_value(self, data_after: Any, data_to_insert: Any) -> None:
        """Inserts data_to_insert after the first occurrence of data_after."""
        curr = self.head
        while curr:
            if curr.data == data_after:
                new_node = Node(data_to_insert, curr.next)
                curr.next = new_node
                if curr == self.tail:
                    self.tail = new_node
                self.size += 1
                print(f"Inserted '{data_to_insert}' after '{data_after}'.")
                return
            curr = curr.next
        print(f"Value '{data_after}' not found in the list. Insertion failed.")
            
    def remove_by_value(self, data_to_remove: Any) -> None:
        """Removes the first occurrence of data_to_remove from the list."""
        if self.head is None:
            print("List is empty. Removal failed.")
            return

        # Case 1: The element to remove is at the head
        if self.head.data == data_to_remove:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            print(f"Removed '{data_to_remove}' from the list.")
            return

        # Case 2: The element is somewhere else in the list
        curr = self.head
        while curr.next:
            if curr.next.data == data_to_remove:
                # If we are removing the tail, update tail pointer
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                self.size -= 1
                print(f"Removed '{data_to_remove}' from the list.")
                return
            curr = curr.next

        print(f"Value '{data_to_remove}' not found in the list. Removal failed.")

    def print(self) -> None:
        """Prints the visual representation of the linked list."""
        if self.head is None:
            print("Linked list is empty")
            return
        
        elements = [str(data) for data in self]
        print(" --> ".join(elements))


def main():
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()


if __name__ == "__main__":
    main()
