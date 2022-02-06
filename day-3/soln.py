# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
input_set = []
country_set = set(input_set)
for i in range(n):
    name = input()
    country_set.add(name)

print(len(country_set))

# num = raw_input()
# dist = set()
# for i in range(int(num)):
#     dist.add(raw_input())
# print len(dist)
