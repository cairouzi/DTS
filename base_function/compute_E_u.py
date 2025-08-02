import math
import numpy as np

#组里EC计算效用 和 组平均效用
def compute_E_u(model,EC_choose,SES_choosed,EC_x_res,SES_price):
    EC_SES_utility = np.zeros((model.group_num,model.num))
    group_utility = np.zeros(model.group_num)
    group_aver_u = np.zeros(model.group_num)
    for h in range(model.group_num):
        for i in range(model.num):
            m = EC_choose[h][i] - 1
            EC_SES_utility[h][i] = model.u1_EC * math.log2(model.u2_EC * EC_x_res[m]) - SES_price[m] * EC_x_res[m]
            group_utility[h] = group_utility[h] + EC_SES_utility[h][i] 
    
    for h in range(model.group_num):
        group_aver_u[h] = group_utility[h] / model.num

    """EC_SES_utility = np.round(EC_SES_utility,3)
    group_aver_u = np.round(group_aver_u,3)"""
    return EC_SES_utility,group_aver_u