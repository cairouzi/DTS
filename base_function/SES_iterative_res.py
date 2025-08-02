import numpy as np
import math


# 寻找SES的最优资源 
# evolutionary equilibrium中设置为 0.01 0.019
def SES_iterative_res(model,EC_x_res,SES_choosed,SES_x_all,SES_x_res,SES_price,SES_cost,cur_dfx_):
    SES_utility_ = np.zeros(model.SES_num)
    opt_x_res = SES_x_res
    epsilon = 0.01
    eta_x = 5
    cur_dfx = np.zeros(model.SES_num)
    for m in range(model.SES_num):
        if SES_choosed[m] != 0:
            SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - (EC_x_res[m] + epsilon) * SES_choosed[m])) + (SES_price[m]  - SES_cost[m]) * (EC_x_res[m] + epsilon) * SES_choosed[m] - model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - (EC_x_res[m] - epsilon) * SES_choosed[m])) + (SES_price[m] - SES_cost[m]) * EC_x_res[m] * SES_choosed[m]
            SES_x_res[m] = SES_x_res[m] + epsilon
            EC_x_res[m] = SES_x_res[m] / SES_choosed[m]
            while SES_x_res[m] >= SES_x_all[m]:
                SES_x_res[m] = SES_x_all[m] - 0.01
                EC_x_res[m] = SES_x_res[m] / SES_choosed[m]

            SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m]  - SES_cost[m]) * EC_x_res[m] * SES_choosed[m] - model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m])) + (SES_price[m] - SES_cost[m]) * EC_x_res[m] * SES_choosed[m]
        
        else:
            SES_utility_[m] = 0
        
        cur_dfx[m] = SES_utility_[m] / 2 * epsilon
        
        if abs(cur_dfx_[m] - cur_dfx[m]) < epsilon:
            break
        else:
            res_x = SES_x_res[m] + eta_x * cur_dfx[m]
            opt_x_res[m] = res_x
            res_x = np.round(res_x,1)
            while res_x > SES_x_all[m]:
                res_x = res_x - 1
                opt_x_res[m] = res_x

    return cur_dfx,opt_x_res