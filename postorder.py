class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Create a function left>right>root
def post_order(root):
    if root is None:
        return
    # Step1: Visit left 
    post_order(root.left)
    # Step2 Visit right
    post_order(root.right)
    # Step3: Visit root
    print(root.data,end=" ")       
# Create a tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

# Function calling

post_order(root)        