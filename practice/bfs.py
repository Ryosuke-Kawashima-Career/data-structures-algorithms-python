from typing import Dict, List, Set, Optional
from collections import deque

def bfs(start: str, end: str, graph: Dict[str, Set[str]], visited: Set[str], path: List[str]) -> bool:
    queue = deque()
    queue.append(start)
    visited.add(start)
    while queue:
        curr = queue.popleft()
        visited.add(curr)
        path.append(curr)
        if curr == end:
            return True
        for neighor in graph.get(curr, set()) - visited:
            queue.append(neighor)
    return False

def main():
    data = {
        "A" : {"B"},
        "B" : {"A", "C", "D"},
        "C" : {"B", "E"},
        "D" : {"B", "E"},
        "E" : {"C", "D", "F"},
        "F" : {"E"}
    }
    visited = set()
    path = []
    bfs("A", "D", data, visited, path)
    for node in path:
        if node == "D":
            print(node)
        else:
            print(f"{node}->", end="")
    
if __name__ == "__main__":
    main()
