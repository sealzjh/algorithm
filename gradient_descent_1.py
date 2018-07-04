# -*- encoding: utf8 -*-


class GradientDecent:

    def __init__(self, rate):
        self.__rate = rate

    def f(self, x):
        return x ** 3 + 2 * x - 3

    def loss(self, x):
        return (self.f(x) - 0) ** 2

    def gradient_descent(self, x):
        delta = 0.00000001
        derivative = (self.loss(x + delta) - self.loss(x)) / delta
        return x - self.__rate * derivative

    def run(self, x):
        for i in range(50):
            x = self.gradient_descent(x)
            print "x = %f, fx = %f" % (x, self.f(x))

if __name__ == '__main__':
    gd = GradientDecent(0.01)

    x = 0
    gd.run(x)
