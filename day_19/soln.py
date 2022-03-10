number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            print('Not a Rrime number')
            break
    else:
        print('It is a Prime number')


else:
    print('Not a prime number')
