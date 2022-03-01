# .difference() returns the elements which are in the set but not in the list to passed to it in the .difference() func.

totalengstudents = int(input())
engstudents = input().split()
totalfrenchstudents = int(input())
frenchstudents = input().split()

c = set(engstudents)
print(len(c.difference(frenchstudents)))

# i can also use '- operation' instead of difference
