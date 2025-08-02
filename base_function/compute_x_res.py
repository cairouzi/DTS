import numpy as np

#选择SES后，组里EC可以获得的资源量
def compute_x_res(model,SES_choosed,SES_x_res,SES_x_all):
    EC_x_res = np.zeros(model.SES_num)
    for m in range(model.SES_num):
        if SES_choosed[m] != 0:
            EC_x_res[m] = SES_x_res[m] / SES_choosed[m]
            EC_x_res[m] = np.round(EC_x_res[m], 1)
            while EC_x_res[m] * SES_choosed[m] >= SES_x_res[m]:
                EC_x_res[m] = EC_x_res[m] - 0.1
        else:
            EC_x_res[m] = 0
    return EC_x_res