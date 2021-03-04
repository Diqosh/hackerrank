def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(sub_string), len(string) + 1):
        a = string[i-len(sub_string):i]
        if a == sub_string:
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)