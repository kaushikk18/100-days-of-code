#  union() returns the numbers which appear atleast once in the given sets

totalengstudents = int(input())
engstudents = input().split()
totalfrenchstudents = int(input())
frenchstudents = input().split()

s = set(engstudents)
print(len(s.union(frenchstudents)))

# i can also use | operation to do the same thing
