class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree
root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)


# Display root and children
print("Root:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)