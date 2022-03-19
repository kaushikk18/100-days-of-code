n = 9474
ams = 0
length = len(str(n))
temp = n
while(temp > 0):
    last_digit = n % 10
    ams += pow(last_digit, length)
    n = n//10

print(ams)
if(ams == n):
    print('The given number is an amstrong number')
else:
    print('The given number is not an amtrong number')
