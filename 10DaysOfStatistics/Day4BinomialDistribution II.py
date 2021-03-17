class MySolution:
    def __init__(self, percent, atLeast, noMore, n):
        self.probab = percent
        self.atLeast = atLeast
        self.noMore = noMore
        self.n = n

    def fact(self, someInteger):
        sum1 = 1
        for i in range(1, someInteger+1):
            sum1 *= i
        return sum1

    def combo(self, n , x):
        return self.fact(n)/(self.fact((n-x)) * self.fact(x))

    def Dis(self,  x):
        return self.combo(self.n, x)*(self.probab**x)*((1-self.probab)**(self.n-x))

    def allDisAtLeast(self):
        sum1 = 0
        while self.atLeast <= self.n:
            sum1 += self.Dis(self.atLeast)
            self.atLeast += 1
        return sum1

    def allDisNoMore(self):
        sum1 = 0
        while self.noMore >= 0:
            sum1 += self.Dis(self.noMore)
            self.noMore -= 1
        return sum1

if __name__ == '__main__':
    percent, all1 = list(map(float, input().split()))
    myClass = MySolution(percent/100, 2, 2, 10)
    print(format(myClass.allDisNoMore(), '.3f'))
    print(format(myClass.allDisAtLeast(), '.3f'))