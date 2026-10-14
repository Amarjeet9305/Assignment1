arr = [40,10,30,20,50]

n = len(arr)

for i in range(n):
    swapped = False

    for j in range(n - 1 -i):
        if arr[j] > arr[j + 1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
    if not swapped:
        break
print("Array is sorted:", arr)            