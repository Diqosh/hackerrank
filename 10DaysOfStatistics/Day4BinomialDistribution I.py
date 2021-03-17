class MySolution:
    def __init__(self, boys, all1, b, n):
        self.probab = boys / all1
        self.atLeast = b
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

    def allDis(self):
        sum1 = 0
        while self.atLeast <= self.n:
            sum1 += self.Dis(self.atLeast)
            self.atLeast += 1
        return sum1


if __name__ == '__main__':
    boys, girls = list(map(float, input().split()))
    myClass = MySolution(boys, boys + girls, 3, 6)
    print(format(myClass.allDis(), '.3f'))










