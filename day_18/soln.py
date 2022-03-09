word = input()
reversed = ''
last_index = len(word)-1


# method 1

def palindrome(word, reversed, last_index):
    for i in range(0, len(word)):
        reversed += word[last_index]
        last_index -= 1

    if(reversed == word):
        print('It is a palindrome')
    else:
        print('Not a palindrome')


# method 2
# def palindrome(word, reversed, last_index):
#     reversed = word[::-1]

#     if(reversed == word):
#         print('It is a palindrome')
#     else:
#         print('Not a palindrome')


palindrome(word, reversed, last_index)
