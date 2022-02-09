def is_leap(year):

    if(1900 <= year):
        leap = False
        # if(year%400 == 0):
        #     leap = True
        # if(year%100 == 0):
        #     leap = False
        # if(year%4 == 0):
        #     leap = True
        # return leap
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return leap
    if (year % 4 == 0):
        return True
    else:
        return False

    return leap


year = int(input())
