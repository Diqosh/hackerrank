if __name__ == '__main__':
    student, subjects = list(map(int, input().split()))
    sheet = list()

    for i in range(subjects):
        sheet.append(list(map(float, input().split())))

    for i in zip(*sheet):
        print(format(sum(i)/len(i), '.1f'))
