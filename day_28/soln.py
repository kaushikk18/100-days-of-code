
def unique(n):
    unique_count = 0
    cnt = [0] * 10

    while(n > 0):

        rem = n % 10
        cnt[rem] += 1
        n = n//10

    for i in range(10):
        if(cnt[i] == 1):
            unique_count += 1

    return print(unique_count)


n = 2234262
unique(n)
