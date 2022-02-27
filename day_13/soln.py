def average(array):
    # your code goes here
    sets = set(arr)
    total = 0
    for element in sets:
        total += element
    avg = total/len(sets)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
