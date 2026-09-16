arr = [30,34,32,55,60,44,45]

size = 4

hash_table = [None]*size

for num in arr:
    index = num % size

    i = 1
    
    while hash_table[index] is not None:
        
        index = (num % size + i * i) % size

        i += 1
        break
    hash_table[index] = num
print(hash_table)        