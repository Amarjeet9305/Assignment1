# Given array
arr = [30, 34, 32, 55, 60, 44, 54]

# Hash table size
size = 10

# Create empty hash table
hash_table = [None] * size

# Insert every number
for ele in arr:

    # Calculate hash index
    index = ele % size

    # If index is already occupied
    while hash_table[index] is not None:

        # Move to the next index
        index = (index + 1) % size

    # Store the number at empty index
    hash_table[index] = ele

# Print the hash table
print(hash_table)