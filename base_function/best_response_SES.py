import numpy as np
import math


# 寻找SES的最优响应函数
def best_response_SES(model,SES_choosed,SES_choosed_,SES_x_all,SES_x_res,SES_x_res_ave,SES_price,SES_cost,SES_utility,SES_utility_lowest):
    SES_utility_ = np.zeros(model.SES_num)
    opt_SES_price = SES_price
    opt_SES_res = SES_x_res
    for m in range(model.SES_num):
        if SES_choosed[m] >= SES_choosed_[m]:
            start_price = SES_price[m]  
            end_price = 1.2  
            step = 0.001 * SES_choosed[m]  
            current_price = start_price + step 
            while current_price <= end_price:      
                SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - SES_x_res[m])) + (current_price - SES_cost[m]) * SES_x_res_ave[m] * SES_choosed[m]
                SES_utility_[m] = np.round(SES_utility_[m],3)
                if SES_utility_[m] > SES_utility[m] :
                    opt_SES_price[m] = current_price
                    break
                current_price += step 

            """for res in np.arange(SES_x_res[m],SES_x_all[m],1):
                SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - res)) + (price - SES_cost[m]) * res           
                if SES_utility_[m] > opt_SES_utility[m] :
                    opt_SES_utility[m] = SES_utility_[m]
                    opt_SES_res[m] = res
                    break"""

            
        else:
            if SES_choosed[m] != 0:
                start_price = SES_price[m]  
                end_price = 1.2  
                step = 0.001 * SES_choosed[m]  
                current_price = start_price + step 
                while current_price <= end_price:      
                    SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - SES_x_res[m])) + (current_price - SES_cost[m]) * SES_x_res_ave[m] * SES_choosed[m]
                    SES_utility_[m] = np.round(SES_utility_[m],3)
                    if SES_utility_[m] > SES_utility[m] :
                        opt_SES_price[m] = current_price
                        break
                current_price += step 

                
            else:
                for price in np.arange(SES_price[m]-0.1,SES_cost[m],-0.1):
                    opt_SES_price[m] = price


            """for res in np.arange(SES_x_res[m],SES_x_all[m],-1):
                SES_utility_[m] = model.u1_SES * math.log2(model.u2_SES * (SES_x_all[m] - res)) + (price - SES_cost[m]) * res           
                if SES_utility_[m] > opt_SES_utility[m] :
                opt_SES_utility[m] = SES_utility_[m]
                opt_SES_res[m] = res
                break"""

    return opt_SES_price