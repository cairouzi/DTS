import random

import numpy as np

class Game():
    def __init__(self, seller, buyer, T, price, coalitions, benefit_S, benefit_B):
        self.seller = seller            
        self.buyer = buyer 
        self.T = T    
        self.price = price
        self.coalitions = coalitions
        self.benefit_S = benefit_S  
        self.benefit_B = benefit_B 

    # 排序函数（按价格排序，但返回ID列表）
    def sort_by_price(self, items, key_func):
        return sorted(items.items(), key=lambda item: key_func(item[1]))

    def negotiate_coalitions(self, S_sorted, B_sorted):
        # 每个卖家都与一个买家形成一个联盟
        matched_b_indices = set()  # 用于跟踪已经匹配的买家原始索引  
        matched_s_indices = set()  # 用于跟踪已经匹配的卖家原始索引
        for i,s in S_sorted:
            for j,b in B_sorted:
                if j in matched_b_indices:
                    continue  # 如果已经匹配，则跳过当前迭代
                else:
                    if b.energy != 0 and s.energy >= b.energy and s.price <= b.price:
                        self.price[(i, j)] = (s.price + b.price) / 2
                        self.coalitions[(i, j)] = 1
                        matched_s_indices.add(i)  # 将卖家原始索引标记为已匹配
                        matched_b_indices.add(j)  # 将买家原始索引标记为已匹配
                        benefit = (b.energy * (self.price[(i, j)] - s.price_) + b.energy * (b.price_ - self.price[(i, j)])) / 2
                        self.benefit_S[i] += benefit
                        self.benefit_B[j] += benefit
                        self.seller[i].energy -= b.energy
                        self.buyer[j].energy = 0
                        # 找到一个匹配后，标记为已匹配，但不需要立即跳出内层循环（因为可能有多个买家满足条件，但这里我们简化处理）
                        # 为了简化，我们只让每个卖家与一个买家交易，然后跳出内层循环
                        break  # 注意：这里假设每个卖家只与一个买家交易，且买家列表是按价格降序排列的，所以第一个满足条件的买家就是最好的
        # 没有被选上就改变自己的price
        for j,b in B_sorted:
            if j in matched_b_indices:
                    continue  # 如果已经匹配，则跳过当前迭代
            else:
                a = b.price
                b.price = np.round(random.uniform(a, 1),2)

        # 没有被选上就改变自己的price
        for i,s in S_sorted:
            if i in matched_s_indices:
                    continue  # 如果已经匹配，则跳过当前迭代
            else:
                a = s.price
                s.price = np.round(random.uniform(a, 1),2)
        return self.coalitions, self.benefit_S, self.benefit_B

    # 执行算法
    def run(self):
        t = 1
        while t <= self.T:
            # 卖家按价格升序
            S_sorted = self.sort_by_price(seller, lambda s: s.price)
            # 买家按价格降序
            B_sorted = self.sort_by_price(buyer, lambda b: -b.price)
            self.coalitions, self.benefit_S, self.benefit_B = self.negotiate_coalitions(S_sorted, B_sorted)
            t += 1 
        return self.coalitions, self.benefit_S, self.benefit_B


# 假设数据结构
class S:
    def __init__(self, id, energy, price, price_):
        self.id = id  # 添加唯一标识符
        self.energy = energy  # 能源
        self.price = price    # 声明的价格
        self.price_ = price_  # 从别的地方购买的成本（？

class B:  
    def __init__(self, id, energy, price, price_):
        self.id = id  # 添加唯一标识符
        self.energy = energy  # 能源
        self.price = price    # 声明的价格
        self.price_ = price_  # 从别的地方购买的成本（？

# 模拟数据
seller = {1: S(1, 150, 0.43, 0.22), 2: S(2, 150, 0.5, 0.25), 3: S(3, 160, 0.48, 0.30), 4: S(4, 155, 0.49, 0.23), 5: S(5, 150, 0.46, 0.24)} 
buyer = {1: B(1, 8, 0.43, 0.79), 2: B(2, 2, 0.16, 0.87), 3: B(3, 6, 0.61, 0.79), 4: B(4, 1, 0.54, 0.98),
5: B(5, 4, 0.4, 0.82), 6: B(6, 4, 0.12, 0.63), 7: B(7, 6, 0.62, 0.88), 8: B(8, 4, 0.57, 0.81), 
9: B(9, 7, 0.58, 0.99), 10: B(10, 4, 0.29, 0.55), 11: B(11, 5, 0.59, 0.87), 12: B(12, 3, 0.21, 0.87),
13: B(13, 10, 0.24, 0.55), 14: B(14, 10, 0.47, 0.65), 15: B(15, 5, 0.63, 0.98), 16: B(16, 6, 0.55, 0.99),
17: B(17, 4, 0.34, 0.82), 18: B(18, 4, 0.61, 0.97), 19: B(19, 6, 0.42, 0.64), 20: B(20, 2, 0.29, 0.51),
21: B(21, 7, 0.56, 0.77), 22: B(22, 3, 0.49, 0.73), 23: B(23, 8, 0.16, 0.98), 24: B(24, 10, 0.72, 0.99),
25: B(25, 3, 0.61, 0.81), 26: B(26, 5, 0.32, 0.92), 27: B(27, 7, 0.45, 0.88), 28: B(28, 2, 0.59, 0.93),
29: B(29, 8, 0.86, 0.92), 30: B(30, 7, 0.14, 0.49), 31: B(31, 6, 0.44, 0.78), 32: B(32, 1, 0.22, 0.52),
33: B(33, 2, 0.53, 0.89), 34: B(34, 7, 0.17, 0.91), 35: B(35, 7, 0.46, 0.7), 36: B(36, 2, 0.22, 0.5),
37: B(37, 9, 0.24, 0.44), 38: B(38, 5, 0.29, 0.79), 39: B(39, 2, 0.27, 0.92), 40: B(40, 7, 0.49, 0.87),
41: B(41, 7, 0.34, 0.92), 42: B(42, 3, 0.2, 0.83), 43: B(43, 6, 0.5, 0.85), 44: B(44, 8, 0.50, 0.91),
45: B(45, 8, 0.31, 0.49), 46: B(46, 10, 0.56, 0.88), 47: B(47, 10, 0.61, 0.94), 48: B(48, 9, 0.47, 0.96),
49: B(49, 6, 0.53, 0.74), 50: B(50, 9, 0.19, 0.4), 51: B(51, 4, 0.46, 0.66), 52: B(52, 10, 0.69, 0.81),
53: B(53, 10, 0.46, 0.62), 54: B(54, 7, 0.41, 0.74), 55: B(55, 3, 0.22, 0.54), 56: B(56, 10, 0.76, 0.94),
57: B(57, 4, 0.59, 0.72), 58: B(58, 9, 0.11, 0.31), 59: B(59, 1, 0.21, 0.78), 60: B(60, 2, 0.62, 0.86),
61: B(61, 1, 0.54, 0.68), 62: B(62, 3, 0.53, 0.94), 63: B(63, 1, 0.54, 0.72), 64: B(64, 4, 0.28, 0.43),
65: B(65, 9, 0.27, 0.38), 66: B(66, 5, 0.11, 0.5), 67: B(67, 7, 0.38, 0.99), 68: B(68, 3, 0.25, 0.88),
69: B(69, 7, 0.55, 0.97), 70: B(70, 3, 0.59, 0.93), 71: B(71, 1, 0.24, 0.99), 72: B(72, 9, 0.20, 0.6),
73: B(73, 7, 0.53, 0.84), 74: B(74, 3, 0.42, 0.95), 75: B(75, 8, 0.24, 0.72), 76: B(76, 6, 0.33, 0.61),
77: B(77, 3, 0.48, 0.98), 78: B(78, 8, 0.47, 0.97), 79: B(79, 5, 0.22, 0.75), 80: B(80, 1, 0.20, 0.48),
81: B(81, 5, 0.22, 0.55), 82: B(82, 1, 0.45, 0.77), 83: B(83, 4, 0.33, 0.99), 84: B(84, 9, 0.43, 0.93),
85: B(85, 5, 0.63, 0.94), 86: B(86, 10, 0.35, 0.56), 87: B(87, 9, 0.24, 0.65), 88: B(88, 4, 0.28, 0.61),
89: B(89, 7, 0.69, 0.99), 90: B(90, 7, 0.35, 0.82), 91: B(91, 9, 0.48, 0.99), 92: B(92, 9, 0.25, 0.75),
93: B(93, 6, 0.73, 0.95), 94: B(94, 9, 0.45, 0.72), 95: B(95, 1, 0.24, 0.64), 96: B(96, 4, 0.35, 0.95),
97: B(97, 8, 0.43, 0.85), 98: B(98, 6, 0.5, 0.61), 99: B(99, 5, 0.45, 0.98), 100: B(100, 9, 0.22, 0.74)}


# 初始化交易相关的数据结构
price = {}
coalitions = {}  # 使用字典来存储联盟信息，键可以是(seller_id, buyer_id)
benefit_S = {seller_id: 0 for seller_id in seller}
benefit_B = {buyer_id: 0 for buyer_id in buyer}

#迭代次数
T = 30  # 简化：只考虑一个交易时段

game = Game(seller, buyer, T, price, coalitions, benefit_S, benefit_B)
coalitions, benefit_S, benefit_B = game.run()

for key, value in benefit_S.items():
    rounded_value = np.round(value, 3)
    print(f"{key}: {rounded_value}")

for key, value in benefit_B.items():
    rounded_value = np.round(value, 3)
    print(f"{key}: {rounded_value}")