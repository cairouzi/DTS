import numpy as np
import math


# 寻找SES的最优价格 
# evolutionary equilibrium中设置为 0.01 0.019
# Nash equilibrium中设置为 0.01 0.014
def SES_iterative_p_res(model,EC_x_res,SES_choosed,SES_x_all,SES_x_res,SES_price,SES_cost,cur_dfx_p_,cur_dfx_x_):
    SES_utility_p = np.zeros(model.SES_num)
    SES_utility_x = np.zeros(model.SES_num)
    opt_SES_price = SES_price
    opt_x_res = SES_x_res
    epsilon_p = 0.01
    epsilon_x = 0.1
    eta_p = 0.014
    eta_x = 2
    cur_dfx_p = np.zeros(model.SES_num)
    cur_dfx_x = np.zeros(model.SES_num)
    for m in range(model.SES_num):
        if SES_choosed[m] != 0:
            SES_utility_p[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m] + epsilon_p - SES_cost[m]) * EC_x_res[m] * SES_choosed[m] - model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m] - epsilon_p - SES_cost[m]) * EC_x_res[m] * SES_choosed[m]
            SES_x_res[m] = SES_x_res[m] + epsilon_x
            EC_x_res[m] = SES_x_res[m] / SES_choosed[m]
            while SES_x_res[m] >= SES_x_all[m]:
                SES_x_res[m] = SES_x_all[m] - 0.01
                EC_x_res[m] = SES_x_res[m] / SES_choosed[m]

            SES_utility_x[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m]  - SES_cost[m]) * EC_x_res[m] * SES_choosed[m] - model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m] - SES_cost[m]) * EC_x_res[m] * SES_choosed[m]

        else:
            SES_utility_p[m] = 0
            SES_utility_x[m] = 0
        
        cur_dfx_p[m] = SES_utility_p[m] / 2 * epsilon_p
        cur_dfx_x[m] = SES_utility_x[m] / 2 * epsilon_x

        if abs(cur_dfx_p_[m] - cur_dfx_p[m]) < epsilon_p and abs(cur_dfx_x_[m] - cur_dfx_x[m]) < epsilon_x:
            break
        else:
            price = SES_price[m] + eta_p * cur_dfx_p[m]
            if price > SES_cost[m] and price < 1.2:
                opt_SES_price[m] = price
            elif price >= 1.2:
                opt_SES_price[m] = 1.2
            else:
                opt_SES_price[m] = SES_cost[m]
            
            res_x = SES_x_res[m] + eta_x * cur_dfx_x[m]
            opt_x_res[m] = res_x
            res_x = np.round(res_x,1)
            while res_x > SES_x_all[m]:
                res_x = res_x - 1
                opt_x_res[m] = res_x
    
    return cur_dfx_p,cur_dfx_x,opt_SES_price,opt_x_res