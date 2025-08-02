#SES停止竞争条件
def stop_flag1(model,EC_choose,EC_choose01):
    flag1 = 0
    for h in range(model.group_num):
        for i in range(model.num):
            """if EC_SES_utility[i] != EC_SES_utility01[i]:
                flag1 = 1"""
            if EC_choose[h][i] != EC_choose01[h][i]:
                flag1 = 1
                break

    return flag1
