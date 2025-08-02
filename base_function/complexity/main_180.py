import sys
import os
import numpy as np


sys.path.append(os.getcwd()+'/test_1')
from base_function.compute_S_u_lowest import compute_S_u_lowest
from base_function.compute_g_s import compute_g_s
from base_function.compute_E_u import compute_E_u
from base_function.compute_S_u import compute_S_u
from base_function.compute_E_transition import compute_E_transition
from base_function.complexity.adj_strategy import adj_strategy
from base_function.stop_flag2 import stop_flag2
from base_function.complexity.SES_iterative import SES_iterative
from base_function.compute_x_res import compute_x_res


#主函数
def main_180(model,EC_choose,group_utility,SES_x_all,SES_x_res,SES_cost,SES_price,SES_utility):

    flag2 = 1
    iterate2 = 0
    total_iter = 0
    SES_choosed_ = np.zeros(model.SES_num)
    SES_utility_lowest = compute_S_u_lowest(model,SES_x_all)  
    cur_dfx_ = np.zeros(model.SES_num)
    while flag2 == 1:
        iterate2 = iterate2 + 1  
        flag = 1
        iterate1 = 0
        while flag == 1:
            iterate1 = iterate1 + 1 
            group_SES,SES_choosed = compute_g_s(model,EC_choose)
            EC_x_res = compute_x_res(model,SES_choosed,SES_x_res,SES_x_all)
            EC_SES_utility,group_aver_u = compute_E_u(model,EC_choose,SES_choosed,EC_x_res,SES_price)
            EC_transition = compute_E_transition(model,EC_SES_utility,group_aver_u)

            #EC停止演化条件
            tran_flag = ( EC_transition <= 0.008 )  #值为 0 or 1
            if np.sum( tran_flag ) == model.sum_num:   #所有人转移概率都小于等于0.05
                flag = 0    

            iter = 0
            #EC更换策略
            if flag == 1:
                EC_choose, iter = adj_strategy(model,EC_choose,EC_x_res,EC_transition,EC_SES_utility,SES_price,group_SES)
                total_iter += iter 

            if iter == 0:
                total_iter += 1
        print("group_aver_u = ",group_aver_u)
        print("EC_choose = ",EC_choose)
        print("iterate1 = ",iterate1)

        SES_utility = compute_S_u(model,EC_x_res,SES_choosed,SES_x_all,SES_x_res,SES_price,SES_cost)
        print("SES_utility = ",SES_utility)
        
        #停止条件
        if iterate2 > 1:
            flag2 = stop_flag2(model,group_aver_u,group_aver_u01,SES_utility,SES_utility01)

        # SES c,x,p change
        if flag2 == 1:
            SES_utility01 = SES_utility
            group_aver_u01 = group_aver_u
            cur_dfx,SES_price = SES_iterative(model,EC_x_res,SES_choosed,SES_x_all,SES_x_res,SES_price,SES_cost,cur_dfx_)
            cur_dfx_ = cur_dfx
            SES_choosed_ = SES_choosed
        print("SES_choosed = ",SES_choosed)
        print("SES_price",SES_price)
    
    print("iterate2 = ",iterate2)
    print("EC_x_res",EC_x_res)
    print("当前交易完成")
    print("\n")
    return SES_utility,SES_choosed,group_SES,EC_x_res,total_iter