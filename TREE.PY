class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


if __name__ == "__main__":
    root = TreeNode("Root")
    node1 = TreeNode("Node 1")
    node2 = TreeNode("Node 2")
    node3 = TreeNode("Node 3")
    
    root.add_child(node1)
    root.add_child(node2)
    node1.add_child(node3)
    
    print(root)
