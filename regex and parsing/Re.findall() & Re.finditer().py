import re

consonants = 'qwrtypsdfghjklzxcvbnmQWERYPSDFGHJKLZXCVBNM'
vowels = 'aeiouAEIOU'

if __name__ == '__main__':
    txt = input()
    x = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',txt)
    if x:
        for i in x:
            print(i)
    else:
        print('-1')

