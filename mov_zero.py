# Wap to Move Zeros: Move all zeroes to the end while keeping the order of non-zero elements.

# Input:
# [0, 1, 0, 3, 12]

# Output:
# [1, 3, 12, 0, 0]

# Create an array containing zeros and non-zero values
arr = [0, 1, 0, 3, 12]    
      
# Slow pointer starts at index 0
slow = 0 
                        
# Fast pointer visits every index from left to right
for fast in range(len(arr)):  
       
# Check if the current element is NOT zero
    if arr[fast] != 0:           

        # Swap the non-zero element with the element at slow pointer
        arr[slow], arr[fast] = arr[fast], arr[slow]
# Move slow pointer one position forward
        slow += 1               
# Print the final array
print(arr)                       