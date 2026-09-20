class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Create a function In-order

def in_order(root):
    if root is None:
        return
    # Step1: Visit left subtree
    
    in_order(root.left) 
    
    # Step2: Visit root
    print(root.data,end=" ")
    
    # Step3: Visit right subtree
    in_order(root.right) 
# Calling a driver code

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


# Function calling

in_order(root)          
    