def Median(lisi):
    lis = sorted(lisi)
    if len(lis) % 2 == 0:
        return format((lis[len(lis) // 2 - 1] + lis[len(lis) // 2]) / 2, '.1f')
    elif len(lis) % 2 == 1:
        return format(lis[len(lis) // 2], '.1f')


def quartles(elements):
    elementsSorted = sorted(elements)

    if len(elements) % 2 == 0:
        yield Median(elementsSorted[:len(elements) // 2])
        yield Median(elementsSorted)
        yield Median((elementsSorted[len(elements) // 2:]))
    else:
        yield Median(elementsSorted[:len(elements) // 2])
        yield Median(elementsSorted)
        yield Median(elementsSorted[len(elements) // 2 + 1:])


if __name__ == '__main__':
    cntElem = int(input())
    elementsSet = list(map(int, input().split()))
    frequence = list(map(int, input().split()))
    elements = list()
    for i in range(len(elementsSet)):
        for c in range(frequence[i]):
            elements.append(elementsSet[i])
    quartlesElem = [float(i) for i in quartles(elements)]
    print(quartlesElem[2] - quartlesElem[0])

