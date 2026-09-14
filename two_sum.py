# We are solving a Two sum array problem using two -pointer approach
# Take a array to represent list
arr = [1,2,4,6,10]

# Define expected output and target

target = 8

#Initilize left pointer

left = 0 

right = len(arr) - 1

#using while loop and if-else condition 

while left < right:
    total = arr[left] + arr[right]
    
    if total == target:
        print("Index position:", left,right)
        print("Index position element", arr[left], arr[right])
        print("Targeted sum:", total)
        break
    
    elif total < target:
        
        left += 1
    else:
        right -= 1    
        