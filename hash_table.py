# Given array
arr = [30, 34, 32, 55, 60]

# Size of our hash table
size = 10

# Create an empty hash table
hash_table = [None] * size

# Go through every number in the array
for num in arr:

    # Calculate the index using hash function
    index = num % size

    # Store the number at calculated index
    hash_table[index] = num

# Print the hash table
print(hash_table)