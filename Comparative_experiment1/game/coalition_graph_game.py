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
            if s.energy > 0:
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
            S_sorted = self.sort_by_price(self.seller, lambda s: s.price)
            # 买家按价格降序
            B_sorted = self.sort_by_price(self.buyer, lambda b: -b.price)
            self.coalitions, self.benefit_S, self.benefit_B = self.negotiate_coalitions(S_sorted, B_sorted)
            t += 1 
        return self.coalitions, self.benefit_S, self.benefit_B
