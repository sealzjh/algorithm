# -*- encoding: utf8 -*-


class GradientDecent:

    def __init__(self, rate):
        self.__rate = rate

    def f(self, x):
        return x[0] + 2 * x[1] + 4

    def loss(self, x):
        return (self.f(x) - 0) ** 2

    def gradient_descent(self, x):
        delta = 0.00000001
        derivative = {}
        derivative[0] = (self.loss([x[0] + delta, x[1]]) - self.loss(x)) / delta
        derivative[1] = (self.loss([x[0], x[1] + delta]) - self.loss(x)) / delta

        x[0] = x[0] - self.__rate * derivative[0]
        x[1] = x[1] - self.__rate * derivative[1]

        return x

    def run(self, x):
        for i in range(150):
            x = self.gradient_descent(x)
            print "x = %f, %f, fx = %f" % (x[0], x[1], self.f(x))

if __name__ == '__main__':
    gd = GradientDecent(0.01)

    x = [-0.5, -1.0]
    gd.run(x)