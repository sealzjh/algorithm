# -*- encoding: utf8 -*-


class HMM:
    """
    隐马尔科夫模型(HMM)
    三个基本问题:
    1. 评估问题 已知状态转移矩阵A，输出矩阵B，和观测序列O，求该观测序列O出现的可能性
    2. 解码问题 已知状态转移矩阵A，输出矩阵B，和观测序列O，找出最有可能产生该观测序列的隐藏状态序列 
    3. 参数学习问题 Π参数学习
    """

    def __init__(self):
        # 隐藏状态
        self.S = ('Sunny', 'Cloudy', 'Rainy')

        # 状态转移
        self.A = {
            'Sunny': {'Sunny': 0.6, 'Cloudy': 0.3, 'Rainy': 0.1},
            'Cloudy': {'Sunny': 0.2, 'Cloudy': 0.3, 'Rainy': 0.5},
            'Rainy': {'Sunny': 0.4, 'Cloudy': 0.1, 'Rainy': 0.5}
        }

        # 初始概率
        self.PI = {'Sunny': 0.5, 'Cloud': 0.3, 'Rainy': 0.2}

        # 观测状态
        self.O = ('Walk', 'Shop', 'Clean')

        # 输出概率
        self.B = {
            'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1},
            'Cloudy': {'Walk': 0.4, 'Shop': 0.3, 'Clean': 0.4},
            'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5}
        }

    def state_observation_prob(self, input):
        prev = ''
        prob = 0
        for index, val in enumerate(input):
            a_prob = self.PI[val[0]] if index == 0 else self.A[prev][val[0]]
            b_prob = self.B[val[0]][val[1]]

            prob = a_prob * b_prob if prob == 0 else prob * a_prob * b_prob
            prev = val[0]

        return prob

if __name__ == '__main__':
    hmm = HMM()

    # 隐藏状态序列及观测序列 出现的概率
    input = [['Sunny', 'Shop'], ['Rainy', 'Walk'], ['Rainy', 'Clean']]
    print "state observation prob:", hmm.state_observation_prob(input)

    # 破解隐藏状态序列
    input = ['Shop', 'Walk', 'Clean', 'Walk']

    # 最大观测序列