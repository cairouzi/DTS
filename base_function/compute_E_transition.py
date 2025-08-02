import numpy as np

#组里EC是否更换策略
def compute_E_transition(model,EC_SES_utility,group_aver_u):
    EC_transition = np.zeros((model.group_num,model.num))
    for h in range(model.group_num):
        for i in range(model.num):
            if EC_SES_utility[h][i] < group_aver_u[h]:
                EC_transition[h][i] = (group_aver_u[h] - EC_SES_utility[h][i]) / group_aver_u[h]
            else:
                EC_transition[h][i] = 0
 
    EC_transition = np.round(EC_transition,4)
    return EC_transition


