import math
import os
import random
import re
import sys

# method1
# def reverseArray(a):
#     dummy_array=''
#     ## rev_arr = arr[len(a)-1::-1]
#     rev_arr = arr[len(a)-1::-1]
#     return rev_arr

# method 2
# def reverseArray(a):
#     dummy_array=[]
#     for i in range(len(a)-1, -1, -1):
#         dummy_array.append(a[i])    
#     return dummy_array

# method 3
def reverseArray(a):
    dummy_array=[]
    x=len(a)-1
    for i in range(len(a)):
        dummy_array.append(a[x])
        x-=1
    return dummy_array    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
