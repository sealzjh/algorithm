# -*- encoding: utf8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class LeastSquare:
    """
    最小二乘法
    z = a + bx
    """

    def __init__(self):
        self.__a = 0
        self.__b = 0

    def show(self, df):
        plt.xlabel('x')
        plt.ylabel('y')
        plt.scatter(df['x'], df['y'], color='r')

        x = np.linspace(0, max(df['x']), 1000)
        y = [self.__a + self.__b * x]
        plt.scatter(x, y, color='black', linewidths=1)

        plt.show()
        plt.close()


    def run(self, data):
        df = pd.DataFrame(data, columns=['x', 'y'])

        n = len(df)
        xy_sum = df['x'].mul(df['y']).sum()
        xx_sum = df['x'].mul(df['x']).sum()
        x_sum = df['x'].sum()
        y_sum = df['y'].sum()

        self.__a = (xx_sum * y_sum - xy_sum * x_sum) / (n * xx_sum - x_sum * x_sum)
        self.__b = (n * xy_sum - x_sum * y_sum) / (n * xx_sum - x_sum * x_sum)

        print "a: ", self.__a
        print "b: ", self.__b
        print "y = %s + %sx" % (self.__a, self.__b)

        self.show(df)

if __name__ == '__main__':
    data = [
            [18, 202],
            [23, 186],
            [25, 187],
            [35, 180],
            [65, 156],
            [54, 169],
            [34, 174],
            [56, 172],
            [34, 174],
            [56, 172],
            [72, 153],
            [19, 199],
            [23, 193],
            [42, 174],
            [18, 198],
            [39, 183],
            [37, 178]
            ]

    least = LeastSquare()
    least.run(data)