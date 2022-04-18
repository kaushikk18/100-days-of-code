def repetition_check(i):
    a = []
    while(i != 0):
        rem = i % 10
        if rem in a:
            return 1
        else:
            a.append(rem)
        i = i//10
    return 0


n1 = int(input())
n2 = int(input())
count = 0

for i in range(n1, n2+1):
    count += repetition_check(i)

print(count)
