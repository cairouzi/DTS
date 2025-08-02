import random

import numpy as np

#EC更换策略

# 设置随机种子
#random_seed = 210    # 4组
random_seed = 42     # 2组
random.seed(random_seed)
np.random.seed(random_seed)


def adj_strategy(model,EC_choose,EC_x_res,EC_transition,EC_SES_utility,SES_price,group_SES):
    flag_3 = 0
    iter = 0
    while flag_3 == 0:   
        #找到随机组中转移概率最大的元素的索引和值  
        random_h = random.randrange(model.group_num)   
        # 初始化最大值和对应的下标列表  
        tran_max_value = float('-inf')  
        tran_max_indices = []  
        # 遍历列表  
        for i, value in enumerate(EC_transition[random_h]):
            if value > tran_max_value:  
                # 如果找到更大的值，更新最大值和对应的下标列表  
                tran_max_value = value  
                tran_max_indices = [i]  
            elif value == tran_max_value:  
                # 如果值等于当前最大值，将下标添加到列表中  
                tran_max_indices.append(i)  
        
        # 随机选一个最大值列表的索引 并获取相关属性
        random_index = random.choice(tran_max_indices)
        random_tran_max_SES = EC_choose[random_h][random_index]
        random_tran_max_price = SES_price[random_tran_max_SES - 1]
        random_tran_max_x_res = EC_x_res[random_tran_max_SES - 1]
        random_tran_max_utility = EC_SES_utility[random_h][random_index]

        #随机一个random_m,效用比它大且满足条件 则更换
        #如果迭代了很多次，还没有找到，就随便选一个SES购买策略 
        found_replacement = False 
        iterate = 0
        while not found_replacement: 
            iterate = iterate + 1
            if iterate < 15:
                random_m = random.randrange(1, model.SES_num + 1) 
                if random_tran_max_SES != random_m:
                    for j, value in enumerate(EC_SES_utility[random_h]):
                        iter += 1
                        if EC_choose[random_h][j] == random_m:
                            if value > random_tran_max_utility: 
                                utility_price = SES_price[random_m - 1]
                                utility_x_res = EC_x_res[random_m - 1]
                                if random_tran_max_x_res < utility_x_res and random_tran_max_price > utility_price:
                                    EC_choose[random_h][random_index] = random_m
                                    found_replacement = True 
                                    flag_3 = 1
                                    break
            else:
                random_m = random.randrange(1, model.SES_num + 1)
                if random_tran_max_SES != random_m:
                    EC_choose[random_h][i] = random_m
                    found_replacement = True 
                    flag_3 = 1
    print("迭代次数",iter)
    return EC_choose, iter