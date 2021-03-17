class MySolution:
    def __init__(self, numerator, denominator, items):
        self.p = numerator/denominator
        self.items = items

    def formula(self):
        return  self.p*(1-self.p)**(self.items-1)

if __name__ == '__main__':
    numerator, denominator = list(map(int, input().split()))
    MyClass = MySolution(numerator, denominator, int(input()))
    print(format(MyClass.formula(), '.3f'))

