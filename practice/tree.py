from typing import List, Optional

class Node:
    def __init__(self, name, designation, parent_node):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = parent_node
        if parent_node is not None:
            parent_node.add_child(self)
    def add_child(self, child):
        self.children.append(child)
    def reset_parent(self, new_parent):
        self.parent.children.remove(self)
        self.parent = new_parent
        new_parent.add_child(self)
    def print(self, key:str):
        if key == "name":
            print(self.name)
        elif key == "designation":
            print(self.designation)
        elif key == "both":
            print(f"{self.name} ({self.designation})")

class Tree:
    def __init__(self):
        self.nodes = []
        self.root = None
    def set_root(self, node: Node):
        self.root = node
    def append(self, node: Node):
        self.nodes.append(node)
    def print_tree(self, key: str):
        """prints nodes by DFS"""
        if self.root is None:
            print("Tree is empty")
            return
        self._dfs(self.root, key, 0)
    
    def _dfs(self, node: Node, key: str, depth: int):
        if node is self.root:
            node.print(key)
        else:
            for _ in range(depth):
                print("    ", end="")
            print("|__", end="")
            node.print(key)
        for child in node.children:
            self._dfs(child, key, depth+1)


def main():
    ceo = Node("Nilupul", "CEO", None)

    cto = Node("Chinmay", "CTO", ceo)
    hr_head = Node("Gels", "HR Head", ceo)

    infra_head = Node("Vishwa", "Infrastructure Head", cto)
    app_head = Node("Aamir", "Application Head", cto)
    recruit_manager = Node("Peter", "Recruitment Manager", hr_head)
    policy_manager = Node("Waqas", "Policy Manager", hr_head)
        
    cloud_manager = Node("Dhaval", "Cloud Manager", infra_head)
    app_manager = Node("Abhijit", "Application Manager", infra_head)

    tree = Tree()
    tree.set_root(ceo)
    tree.append(cto)
    tree.append(hr_head)
    tree.append(infra_head)
    tree.append(app_head)
    tree.append(recruit_manager)
    tree.append(policy_manager)
    tree.append(cloud_manager)
    tree.append(app_manager)
    tree.print_tree(key="both")

if __name__ == "__main__":
    main()
