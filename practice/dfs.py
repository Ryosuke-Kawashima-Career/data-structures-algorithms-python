from typing import Dict, List, Set

def dfs(v: str, parent: str, graph: Dict[str, Set[str]], visited: Set[str], decendants: Set[str]):
    """Calculates decendants of a node"""
    if v in visited:
        return
    visited.add(v)
    for next in graph[v]:
        if next not in visited:
            decendants.add(next)
            dfs(next, v, graph, visited, decendants)
    return
    

def main():
    data = {
        "karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        "tanuj": {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
    }
    visited = set()
    decendants = set()
    dfs("karan", "", data, visited, decendants)
    print(f"Decendants of karan: {decendants}")

if __name__ == "__main__":
    main()
