from typing import List, Optional
class HashTableChain:
    def __init__(self, size: int = 100):
        self.MOD = size
        self.arr: List[List[Optional[str]]] = [[] for _ in range(self.MOD)]
    
    def get_hash(self, key: str) -> int:
        """Calculate the hash value in the way of decimal representation of the string."""
        hash_value = 0
        for character in key:
            hash_value = (hash_value * 10 + ord(character)) % self.MOD
        return hash_value % self.MOD

    def __getitem__(self, key: str) -> List[Optional[str]]:
        """Get the values by key."""
        hash_value = self.get_hash(key)
        return self.arr[hash_value].copy()
    def __setitem__(self, key: str, value: str) -> None:
        """Set the value by key."""
        hash_value = self.get_hash(key)
        self.arr[hash_value].append(value)
    def __contains__(self, key: str) -> bool:
        """Check if the key exists in the hash table."""
        hash_value = self.get_hash(key)
        return len(self.arr[hash_value]) > 0
    def __delitem__(self, key: str) -> None:
        """Delete the key-value pair by key."""
        hash_value = self.get_hash(key)
        self.arr[hash_value] = []

def main():
    # Get key and value
    hash_table = HashTableChain()
    hash_table["name"] = "Alice"
    hash_table["age"] = "30"
    hash_table["city"] = "New York"

    print(hash_table["name"])  # Output: Alice
    if "age" in hash_table:
        print("Key 'age' exists in the hash table.")
        print(hash_table["age"])  # Output: 30
    else:
        print("Key 'age' not found")

if __name__ == "__main__":
    main()
    