from traceback import print_tb


str = input()
reversed_str = ''

length = len(str)
last_index = length-1

for i in range(0, length):
    reversed_str += str[last_index]
    last_index -= 1

print(reversed_str)
