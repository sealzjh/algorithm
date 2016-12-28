# -*- encoding: utf8 -*-

import random
import math
import matplotlib.pyplot as plt  

class GA:
        
    def __init__(self, s, n, g, c, e):
        self.scale = s      #种群规模
        self.city_num = n   #染色体数量(城市数量)
        self.__max_gen = g  #运行代数
        self.__pc = c       #交叉率
        self.__elite = e    #每代多少胜出者
   
    #交叉
    def crossover(self, tour1, tour2):
        c1 = random.randint(0, len(tour1['tour'])-1)
        c2 = random.randint(0, len(tour1['tour'])-1)

        while c1 == c2:
            c2 = random.randint(0, len(tour1['tour'])-1)

        if c1 > c2:
            c1, c2 = c2, c1

        tour_part = tour1['tour'][c1:c2]

        new_tour = []
        index = 0
        for i in range(len(tour2['tour'])):
            if index == c1:
                for item in tour_part:
                    new_tour.append(item)

            if(tour2['tour'][i] not in tour_part):
                new_tour.append(tour2['tour'][i])
            index+=1

        return self.get_tour_detail(new_tour)

    #变异
    def mutate(self, tour):
        c1 = random.randint(0, len(tour['tour'])-1)
        c2 = random.randint(0, len(tour['tour'])-1)

        while c1 == c2:
            c2 = random.randint(0, len(tour['tour'])-1)

        new_tour = []
        for i in range(len(tour['tour'])):
            if i == c1:
                new_tour.append(tour['tour'][c2])
            elif i == c2:
                new_tour.append(tour['tour'][c1])
            else:
                new_tour.append(tour['tour'][i])

        return self.get_tour_detail(new_tour)
    
    #随机生成城市坐标
    def get_random_city(self):
        c = {
            'x': random.randint(1, 99),
            'y': random.randint(1, 99)
        }
        
        return c
       
    #排序
    def sort(self, tours):
        tours_sort = sorted(tours, key=lambda x:x['score'], reverse=True)

        return tours_sort

    #获取距离
    def get_distance(self, c1, c2):
        xd = abs(c1['x'] - c2['x'])
        yd = abs(c1['y'] - c2['y'])
        distance = math.sqrt(xd * xd + yd * yd)
        
        return distance
        
    #适应性函数 距离越小适应值越大
    def get_score(self, distance):

        return 1/(distance + 1);
 
    #随机获得一条路径
    def get_tour(self):
        tour = []
        for key, value in self._citys.items():
            tour.append(key)

        random.shuffle(tour)

        return self.get_tour_detail(tour)

    def get_tour_detail(self, tour):
        tmp = None
        distance = 0
        for item in tour:
            distance_tmp = 0
            if tmp is not None:
                distance_tmp = self.get_distance(self._citys[tmp], self._citys[item])
                distance+= distance_tmp

            tmp = item

        return {'tour': tour, 'distance': distance, 'score': self.get_score(distance)}

    #初始种群
    def initialise(self):
        tours = []
        for i in range(self.scale):
            tour = self.get_tour()
            tours.append(tour)

        return tours

    #获取当前种群中最优个体
    def get_fittest(self, tours):
        tmp = None
        for item in tours:
            if tmp is None or item['score'] > tmp['score']:
                tmp = item

        return tmp
    
    #随机生成城市点
    def init_citys(self):
        self._citys = {}
        for i in range(self.city_num):
            c = self.get_random_city()
            self._citys[i+1] = c

    #绘图
    def show(self, tour):
        plt.bar(left = 0,height = 100, width = 100, color=(0, 0, 0, 0), edgecolor=(0, 0, 0, 0))
        plt.title(u'tsp问题')
        plt.xlabel('total distance: %s m' % tour['distance'])

        x = []
        y = []
        i = 0
        for item in tour['tour']:
            city = self._citys[item]
            x.append(city['x'])
            y.append(city['y'])

            i+=1
            if i == 1:
                plt.plot(city['x'], city['y'],'or')
            else:
                plt.plot(city['x'], city['y'],'bo')

        plt.plot(x, y, 'g')
        plt.xlim(0.0, 100)
        plt.ylim(0.0, 100)
        plt.show()

    def run(self):
        self.init_citys()
        pop = self.initialise()
        old_fittest = self.get_fittest(pop)

        topelite = int(self.scale * self.__elite)

        same_num = 0
        max_same_num = 30
        max_score = 0
        for i in range(self.__max_gen):
            ranked = self.sort(pop)
            pop = ranked[0:topelite]

            fittest = self.get_fittest(pop)
            if fittest['score'] > max_score: 
                same_num = 0
                max_score = fittest['score']
            else:
                same_num+=1

            #最大分数保持n次一直没有变化则退出
            if same_num > max_same_num:
                break

            while len(pop) < self.scale:
                if random.random() < self.__pc:
                    c1 = random.randint(0, topelite)
                    c2 = random.randint(0, topelite)
                    while c1 == c2:
                        c2 = random.randint(0, topelite)

                    tour = self.crossover(ranked[c1], ranked[c2]) #交叉
                else:
                    c = random.randint(0, topelite - 1)
                    tour = self.mutate(ranked[c]) #变异

                pop.append(tour)

        print 'total gen:', i

        print 'old fittest:'
        print old_fittest
#        self.show(old_fittest)

        print 'new fittest:'
        new_fittest = self.get_fittest(pop)
        print new_fittest
        self.show(new_fittest)

if __name__ == '__main__':
    ga = GA(30, 10, 1000, 0.8, 0.2);
    ga.run()
