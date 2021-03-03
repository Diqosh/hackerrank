def Mean(lis):
    return format(sum(lis) / len(lis), '.1f')


def sumSquareMinusMean(nums, mean):
    return sum([(i - float(mean)) ** 2 for i in nums])


if __name__ == '__main__':
    numCnt = int(input())
    nums = list(map(int, input().split()))

    m = Mean(nums)
    s = sumSquareMinusMean(nums, m)

    print(format((s/numCnt)**0.5, '.1f'))
