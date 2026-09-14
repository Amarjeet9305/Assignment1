# WAP to check sentence is palindrome 'or' 'not'
#Example1: madam is both side read meaning is same is a palindrome
# Example2: racecar is palindrome

# Store the string 
str = input("Enter a string:")                 

left = 0                       # Set the left pointer at the first character

right = len(str) - 1          # Set the right pointer at the last character

str_palindrome = True           # Assume the string is a palindrome initially

while left < right:            # Continue until the two pointers meet

    # Compare characters at the left and right positions
    if str[left] != str[right]:
        str_palindrome = False  # If characters are different, it is not a palindrome
        break                  # Stop the loop because we found a mismatch

    left += 1                  # Move the left pointer one position to the right
    right -= 1                 # Move the right pointer one position to the left

if str_palindrome:              # Check whether the string is still considered a palindrome
    print("Palindrome")        # Print this if all characters matched
else:
    print("Not Palindrome")    # Print this if any characters did not match