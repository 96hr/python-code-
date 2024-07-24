class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        
        if root.left is None and root.right is None:
            return None

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

if __name__ == "__main__":
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        root = insert(root, key)

    print("Inorder traversal before deletion:")
    inorder(root)
    print()

    key_to_delete = 20
    root = deleteNode(root, key_to_delete)

    print(f"\nInorder traversal after deleting {key_to_delete}:")
    inorder(root)
    print()
