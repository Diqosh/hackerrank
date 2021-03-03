
def cmp(elem):
    return [-elem[1], elem[0]]

def printMean(lis):
    print(format(sum(lis) / len(lis), '.1f'))


def printMedian(lisi):
    lis = sorted(lisi)
    if len(lis) % 2 == 0:
        print(format((lis[len(lis) // 2 - 1] + lis[len(lis) // 2]) / 2, '.1f'))
    elif len(lis) % 2 == 1:
        print(lis[len(lis) // 2])


def printMode(lis):
    dic = {}
    for i in lis:
        dic[i] = dic.get(i, 0) + 1
    sortedDic = sorted(dic.items(), key=cmp)
    print(sortedDic[0][0])



if __name__ == '__main__':
    a = int(input())
    ints = list(map(int, input().split()))
    printMean(ints)
    printMedian(ints)
    printMode(ints)
