def swap_case(s):
    new_str = ''
    for charac in s:
        if charac.isupper() == True:
            charac = charac.lower()
            new_str += charac
        else:
            charac = charac.upper()
            new_str += charac
    return new_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
