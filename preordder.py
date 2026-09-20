class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Create a Function Pre-order(root<left< right)        
def pre_order(root):
    if root is None:
        return       
    # Step1: visit root
    print(root.data, end=" ")
    
    # Step2: Visit left subtree
    pre_order(root.left)
    
    # Step3: Visit right
    
    pre_order(root.right)

# Create a tree with element

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

# Function calling

pre_order(root)     