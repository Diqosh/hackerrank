if __name__ == '__main__':
    a = int(input())
    x = list(map(int, input().split()))
    w = list(map(int, input().split()))
    sum1 = 0
    for i in range(a):
        sum1 += x[i] * w[i]
    sum2 = sum(w)

    print(round(sum1/sum2, 1))