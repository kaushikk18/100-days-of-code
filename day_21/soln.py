# largest element in an array
arr = [2, 323, 34, 43, 231, 4345, 213]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print('largest element is', largest)
