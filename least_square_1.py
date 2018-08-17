# -*- encoding: utf8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class LeastSquare:
    """
    z = ax + b
    """

    def __init__(self, data, rate):
        self.__df = pd.DataFrame(data, columns=['x', 'h'])
        self.__rate = rate

    def loss(self, x):
        return (self.__df['h'].sub(x[1]).sub(self.__df['x'].mul(x[0])) ** 2).sum() / 2

    def gradient_descent(self, x):
        delta = 0.00000001
        derivative = {}
        derivative[0] = (self.loss([x[0] + delta, x[1]]) - self.loss(x)) / delta
        derivative[1] = (self.loss([x[0], x[1] + delta]) - self.loss(x)) / delta

        x[0] = x[0] - self.__rate * derivative[0]
        x[1] = x[1] - self.__rate * derivative[1]

        return x

    def show(self, df, x):
        plt.xlabel('x')
        plt.ylabel('h')
        plt.scatter(df['x'], df['h'], color='r')

        xx = np.linspace(0, max(df['x']), 1000)
        yy = [x[0] * xx + x[1]]
        plt.scatter(xx, yy, color='black', linewidths=1)

        plt.show()
        plt.close()

    def run(self, x):
        for i in range(100):
            x = self.gradient_descent(x)
            print "a = %f, b = %f, less = %f" % (x[0], x[1], self.loss(x))

        self.show(self.__df, x)

if __name__ == '__main__':
    data = [
        [2, 5],
        [3, 7],
        [5, 13],
        [8, 17],
        [9, 19],
        #[10, 21],?
    ]
    gd = LeastSquare(data, 0.01)

    x = [0.0, 0.0]
    gd.run(x)