import numpy as np
import math


# 寻找SES的最优价格 
# evolutionary equilibrium中设置为 0.01 0.019
def SES_iterative_(model,EC_x_res,SES_choosed,SES_x_all,SES_x_res,SES_price,SES_cost,cur_dfx_):
    SES_utility_ = np.zeros(model.SES_num)
    opt_SES_price = SES_price
    epsilon = 0.01
    eta_p = 0.015
    cur_dfx = np.zeros(model.SES_num)
    for m in range(model.SES_num):
        if SES_choosed[m] != 0:
            SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m] + epsilon - SES_cost[m]) * EC_x_res[m] * SES_choosed[m] - model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m] - epsilon - SES_cost[m]) * EC_x_res[m] * SES_choosed[m]
        else:
            SES_utility_[m] = 0
        
        cur_dfx[m] = SES_utility_[m] / 2 * epsilon
        
        if abs(cur_dfx_[m] - cur_dfx[m]) < epsilon:
            break
        else:
            price = SES_price[m] + eta_p * cur_dfx[m]
            if price > SES_cost[m] and price < 1.2:
                opt_SES_price[m] = price
            elif price >= 1.2:
                opt_SES_price[m] = 1.2
            else:
                opt_SES_price[m] = SES_cost[m]

    return cur_dfx,opt_SES_price