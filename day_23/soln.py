s1 = 'triangle'
s2 = 'integral'

if(len(s1) != len(s2)):
    print('Not an anagram')
else:
    if(sorted(s1) == sorted(s2)):
        print('The given strings are anagrams')
    else:
        print('Not an anagram')
