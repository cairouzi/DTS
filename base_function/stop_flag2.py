#SES停止竞争条件
def stop_flag2(model,group_aver_u,group_aver_u01,SES_utility,SES_utility01):
    flag2 = 0
    """for i in range(model.group_num):
        if group_aver_u01[i] != group_aver_u[i]:
            flag2 = 1
            break

    for i in range(model.SES_num):
        if SES_utility01[i] != SES_utility[i]:
            flag2 = 1
            break"""
    for i in range(model.group_num):
        if abs(group_aver_u01[i] - group_aver_u[i]) > 0.1:
            flag2 = 1
            break   
    
    for i in range(model.SES_num):
        if abs(SES_utility01[i] - SES_utility[i]) > 0.1:
            flag2 = 1
            break
    return flag2
