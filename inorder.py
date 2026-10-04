# 


class Node():
    def __init__(self,data):   # In order traversal: left< root < right
        self.data = data
        self.left =None
        self.right = None
        
    # Create a function in_order traversal
    
def in_order(root):
    if root is None:
        return
    # Step: Visit left subtree
    in_order(root.left)  
        
    # Step2: Visit root
    print(root.data, end=" ")
        
    # Step3: Visit right subtree
    in_order(root.right) 

# Create a tree
root = Node(1)

root.left = Node(2)
root.left = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


# Function calling or Driver code calling

in_order(root)

#    
    

    