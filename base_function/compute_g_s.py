import numpy as np

#组里EC随机选SES
def compute_g_s(model,EC_choose):
    group_SES = np.zeros((model.group_num, model.SES_num))
    SES_choosed = np.zeros(model.SES_num)
    for h in range(model.group_num):
        for i in range(model.num):
            m = EC_choose[h][i] - 1
            group_SES[h][m] = group_SES[h][m] + 1
            SES_choosed[m] = SES_choosed[m] + 1
    return group_SES,SES_choosed