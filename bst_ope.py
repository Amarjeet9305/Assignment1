class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Find minimum
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # Delete
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            # No child
            if root.left is None and root.right is None:
                return None

            # Only right child
            if root.left is None:
                return root.right

            # Only left child
            if root.right is None:
                return root.left

            # Two children
            successor = self.find_min(root.right)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)

        return root


# Create BST
bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

# Before deletion
print("Before deletion:")
bst.inorder(bst.root)

# Delete 20
bst.root = bst.delete(bst.root, 20)

print("\nAfter deleting 20:")
bst.inorder(bst.root)

# Delete 30
bst.root = bst.delete(bst.root, 30)

print("\nAfter deleting 30:")
bst.inorder(bst.root)

# Delete 50
bst.root = bst.delete(bst.root, 50)

print("\nAfter deleting 50:")
bst.inorder(bst.root)