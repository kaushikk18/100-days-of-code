def total_cost(r1, n1, r2, hr):
    if(hr > n1):
        cost = (r1*n1)+(r2*(hr-n1))
    else:
        cost = n1*r1
    print(cost)  # 120


r1 = int(input())  # 20
n1 = int(input())  # 4
r2 = int(input())  # 40
x = int(input())  # 300
hr = (x+59)//60

total_cost(r1, n1, r2, hr)
