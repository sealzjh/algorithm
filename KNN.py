# -*- encoding: utf8 -*-

import numpy as np
import operator


class KNN:

    def __init__(self, k):
        self.__k = k

    def init_goup_labels(self):
        group = np.array([[1.0, 1.1],
                          [1.0, 1.0],
                          [0.0, 0.0],
                          [0, 0.1]])
        labels = ['A', 'A', 'B', 'B']

        return group, labels

    def knn_label(self, input_x, groups, labels, k):
        diff_mat = np.tile(input_x, (groups.shape[0], 1)) - groups
        # 欧氏距离 sqrt(sum(pow(xi - x)))
        distances = (diff_mat ** 2).sum(axis=1) ** 0.5
        sorted_distances = distances.argsort()

        label_count = {}
        for index in range(k):
            label = labels[sorted_distances[index]]
            label_count[label] = label_count.get(label, 0) + 1

        sorted_label_count = sorted(label_count.iteritems(), key = operator.itemgetter(1), reverse=True)
        return sorted_label_count[0][0]

    def run(self):
        groups, labels = self.init_goup_labels()

        input_x = [0.1, 0.1]

        x_label = self.knn_label(input_x, groups, labels, self.__k)

        print input_x, 'label is: ', x_label

if __name__ == '__main__':
    KNN(3).run()
