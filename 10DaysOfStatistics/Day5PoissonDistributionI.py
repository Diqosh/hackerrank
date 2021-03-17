import math


def fact(a):
    cnt = 1
    while a > 0:
        cnt *= a
        a -= 1
    return cnt


class MySolution:
    def __init__(self, av, var):
        self.average = av
        self.var = var

    def formula(self):
        return ((self.average ** self.var) * (math.e ** (-self.average))) / fact(self.var)


if __name__ == '__main__':
    average = float(input())
    var = int(input())
    MyClass = MySolution(average, var)
    print(format(MyClass.formula(), '.3f'))
