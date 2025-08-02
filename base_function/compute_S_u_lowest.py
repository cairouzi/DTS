import math
import numpy as np

#组里EC计算效用
def compute_S_u_lowest(model,SES_x_all):  
    SES_utility_lowest = np.zeros(model.SES_num)
    for m in range(model.SES_num):
        SES_utility_lowest[m] = model.u1_SES * math.log2(model.u2_SES * SES_x_all[m])
    
    SES_utility_lowest = np.round(SES_utility_lowest,3)
    return SES_utility_lowest