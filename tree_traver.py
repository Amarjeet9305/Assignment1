class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert node
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Inorder: Left → Root → Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")


# Preorder: Root → Left → Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left → Right → Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)


# Traversals
print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)