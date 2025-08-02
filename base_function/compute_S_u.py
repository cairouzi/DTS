import math
import numpy as np

#组里SES计算效用
def compute_S_u(model,EC_x_res,SES_choosed,SES_x_all,SES_x_res,SES_price,SES_cost):  
    SES_utility = np.zeros(model.SES_num)
    for m in range(model.SES_num):
        SES_utility[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - EC_x_res[m] * SES_choosed[m] )) + (SES_price[m] - SES_cost[m]) * EC_x_res[m] * SES_choosed[m]
    #SES_utility = np.round(SES_utility,3)
    return SES_utility