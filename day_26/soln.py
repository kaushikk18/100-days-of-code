
# def rotate_by_one(arr):
#     for i in range(n-1):
#         arr[i] = arr[i+1]


# def rotate(arr, r):
#     for i in range(r):
#         rotate_by_one(arr)

def rotateList(arr, r, n):
    arr[:] = arr[r:n]+arr[0:r]


n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
r = int(input())
rotateList(arr, r, n)
for i in range(n):
    print(arr[i], end=" ")
