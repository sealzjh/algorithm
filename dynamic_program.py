# -*- encoding: utf8 -*-

"""
动态规划做钢条切割
参考: https://blog.csdn.net/u013309870/article/details/75193592
"""


class RecurCut:
    """
    递归方式实现
    """

    def __init__(self, price_dict):
        self.price_dict = price_dict
        self.count = 0

    def run(self, length):
        if length <= 0:
            return 0

        price = 0
        for index in range(length):
            i = index + 1
            price = max(price, self.price_dict.get(i, 0) + self.run(length - i))

        self.count += 1
        return price


class MemoCut:
    """
    从上到下递归方式实现
    """

    def __init__(self, price_dict):
        self.price_dict = price_dict
        self.count = 0

        self.cut_rs = dict()

    def run(self, length):
        if length <= 0:
            return 0

        if length in self.cut_rs:
            return self.cut_rs[length]

        price = 0
        for index in range(length):
            i = index + 1
            self.cut_rs[length - i] = self.run(length - i)
            price = max(price, self.price_dict.get(i, 0) + self.cut_rs[length - i])

        self.count += 1
        return price


class ButtomUpCut:
    """
    从下到上递推方式实现
    """

    def __init__(self, price_dict):
        self.price_dict = price_dict
        self.count = 0

        self.cut_rs = dict()

        for key in price_dict:
            price = 0

            for index in range(key):
                i = index + 1

                price = max(price, self.price_dict.get(i, 0) + self.cut_rs.get(key-i, 0))

            self.count += 1
            self.cut_rs[key] = price

    def run(self, length):
        return self.cut_rs[length]


def max(n1, n2):
    if n1 > n2:
        return n1

    return n2


def load_data():
    price_dict = {
              1: 1,
              2: 5,
              3: 8,
              4: 9,
              5: 10,
              6: 17,
              7: 17,
              8: 20,
              9: 24,
              10: 30,
              }

    return price_dict


if __name__ == '__main__':

    price_dict = load_data()

    recur_cut = RecurCut(price_dict)
    print "RecurCut price: %s, count: %s" % (recur_cut.run(5), recur_cut.count)

    memo_cut = MemoCut(price_dict)
    print "MemoCut price: %s, count: %s" % (memo_cut.run(5), memo_cut.count)

    button_up_cut = ButtomUpCut(price_dict)
    print "ButtomUpCut price: %s, count: %s" % (button_up_cut.run(5), button_up_cut.count)
