#对一些数据进行设置
class Model():
    def __init__(self,group_num,num,sum_num,SES_num,u1_EC,u2_EC,u1_SES,u2_SES):
        self.group_num = group_num   #组数量
        self.num = num               #组里的人数
        self.sum_num = sum_num       #EC总人数 = 组数 * 组人数                         
        self.SES_num = SES_num       #SES数量
        self.u1_EC = u1_EC                
        self.u2_EC = u2_EC
        self.u1_SES = u1_SES
        self.u2_SES = u2_SES