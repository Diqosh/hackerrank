class MySolution:
    def __init__(self, numerator, denominator, items):
        self.p = numerator/denominator
        self.items = items

    def formula(self, a):
        return self.p*(1-self.p)**(a-1)

    def sum(self):
        sum1 = 0
        while self.items != 0:
            sum1 += self.formula(self.items)
            self.items -= 1
        return sum1


if __name__ == '__main__':
    numerator, denominator = list(map(int, input().split()))
    MyClass = MySolution(numerator, denominator, int(input()))
    print(format(MyClass.sum(), '.3f'))

