#  intersection() returns the numbers which appear in both of the given sets

totalengstudents = int(input())
engstudents = input().split()
totalfrenchstudents = int(input())
frenchstudents = input().split()

s = set(engstudents)
print(len(s.intersection(frenchstudents)))

# i can also use & operation to do the same thing
