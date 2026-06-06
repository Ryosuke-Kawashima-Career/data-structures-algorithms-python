from typing import List, Dict, Tuple, Set
from pydantic import BaseModel
class Graph(BaseModel):
    graph: Dict[str, List[Tuple[str, int]]]
    def new(self, nodes: List[str]):
        self.graph = {node: [] for node in nodes}
    def add_edge(self, start: str, end: str, weight: int):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))
    def get_shortest_path(self, start: str, end: str) -> Tuple[bool, List[str]]:
        distances = {node: float('inf') for node in self.graph.keys()}
        distances[start] = 0
        visited = set()
        path = []
        is_reachable, sub_path = self._get_shortest_path(start, end, visited, distances, path)
        if is_reachable:
            return True, sub_path
        else:
            return False, []
        
    def _get_shortest_path(self, start: str, end: str, visited: Set[str], distances: Dict[str, int], path: List[str]) -> Tuple[bool, List[str]]:
        if start == end:
            return True, [end]
        visited.add(start)
        path.append(start)
        for (next_node, weight) in self.graph[start]:
            if next_node not in visited and distances[start] + weight < distances[next_node]:
                is_reachable, sub_path = self._get_shortest_path(next_node, end, visited, distances, path)
                if is_reachable:
                    return True, path + sub_path
        path.pop()
        return False, []

