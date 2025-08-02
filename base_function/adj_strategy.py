import random

import numpy as np

#EC更换策略
def adj_strategy(model,EC_choose,EC_x_res,EC_transition,EC_SES_utility,SES_price,group_SES):
    flag_3 = 0
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

    """# 初始化一个列表的列表来存储每个组转移概率最大的元素的索引  
    tran_max_indices = [[] for _ in range(model.group_num)]
    tran_max_values =  np.zeros(model.group_num) 
    # 遍历列表
    for h in range(model.group_num):  
        max_value_in_group = float('-inf')  
        for i, value in enumerate(EC_transition[h]):  
            if value > max_value_in_group:  
                # 如果在当前组中找到更大的值，更新当前组的最大值和索引列表  
                max_value_in_group = value  
                tran_max_indices[h] = [i]  # 重置索引列表为只包含当前索引  
            elif value == max_value_in_group:  
                # 如果值等于当前组的最大值，将当前索引添加到当前组的索引列表中  
                tran_max_indices[h].append(i) 
            tran_max_values[h] =  max_value_in_group 
    
    tran_max_indices = np.array(tran_max_indices, dtype=object)

    flag_3 = 0
    while flag_3 == 0:
        #找到转移概率最大的元素的组
        max_h = np.argmax(tran_max_values)
        # 从最大值对应的下标列表中随机选择一个下标  
        random_tran_max_index = random.choice(tran_max_indices[max_h])
        random_tran_max_SES = EC_choose[max_h][random_tran_max_index]
        random_tran_max_price = SES_price[random_tran_max_SES - 1]
        random_tran_max_x_res = EC_x_res[random_tran_max_SES - 1]
        random_tran_max_utility = EC_SES_utility[max_h][random_tran_max_index]

        #随机一个random_m,效用比它大且满足条件 则更换
        # 遍历列表  
        found_replacement = False 
        iterate = 0
        while not found_replacement: 
            iterate = iterate + 1
            if iterate < 25:
                random_m = random.randrange(1, model.SES_num + 1) 
                # 生成1到model.SES_num的随机整数
                if random_tran_max_SES != random_m:
                    for j, value in enumerate(EC_SES_utility[max_h]):
                        if EC_choose[max_h][j] == random_m:
                            if value > random_tran_max_utility: 
                                utility_price = SES_price[random_m - 1]
                                utility_x_res = EC_x_res[random_m - 1]
                                if random_tran_max_x_res < utility_x_res and random_tran_max_price > utility_price:
                                    EC_choose[max_h][random_tran_max_index] = EC_choose[max_h][j]
                                    found_replacement = True
                                    flag_3 = 1 
                                    break
            else:
                random_m = random.randrange(1, model.SES_num + 1)
                EC_choose[max_h][random_tran_max_index] = random_m
                found_replacement = True 
                flag_3 = 1 """
        
        
        
    return EC_choose