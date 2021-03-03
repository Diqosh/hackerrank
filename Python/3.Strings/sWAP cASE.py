def swap_case(txt):
    newtxt = str()
    for i in txt:
        if i.isupper():
            newtxt += i.lower()
        elif i.islower():
            newtxt += i.upper()
        else:
            newtxt += i
    return newtxt


if __name__ == '__main__':
    # s = input()
    # result = swap_case(s)
    # print(result)
    print(''.join([i.upper() if i.islower() else i.lower() for i in input()]))
