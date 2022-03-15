# method 1
# str = 'violetypatury'
# vowels = 0
# consonents = 0

# for i in str:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         vowels += 1
#     else:
#         consonents += 1

# print('The number of vowels are', vowels,
#       'and the number of consonents are', consonents)


# method 2
str = 'bdbciwchehcervevhrvcwd bcwdfrieroucsackxeewurtiyeow'
vowels = 0
consonents = 0

for i in str:
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        vowels += 1
    else:
        consonents += 1

print('The number of vowels are', vowels,
      'and the number of consonents are', consonents)
