n = int(input())
arr = []
mu = []
nu = []
for i in range(n):
    x = int(input())
    arr.append(x)

for i in range(n):
    if arr[i] % 10 == 0:
        nu.append(arr[i])
    else:
        mu.append(arr[i])
print(mu+nu)
