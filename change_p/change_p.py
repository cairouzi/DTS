import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
# from initialize import Model
from base_function.main import main
import value_1
import value_2
import value_3
import value_4
import value_5


#初始化设置 共100人
model = initialize.Model(5,20,100,5,3,100,1,5)
EC_choose = np.array(value_1.EC_choose)
EC_choose01 = np.zeros((model.group_num,model.num))

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.group_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

SES_utility,SES_choosed,group_SES = main(model,value_1.EC_choose,group_utility,value_1.SES_x_all,value_1.SES_x_res,value_1.SES_cost,value_1.SES_price1,SES_utility)
y1_100 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_100 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

SES_utility,SES_choosed,group_SES = main(model,value_1.EC_choose,group_utility,value_1.SES_x_all,value_1.SES_x_res,value_1.SES_cost,value_1.SES_price2,SES_utility)
y2_100 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_100 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

SES_utility,SES_choosed,group_SES = main(model,value_1.EC_choose,group_utility,value_1.SES_x_all,value_1.SES_x_res,value_1.SES_cost,value_1.SES_price3,SES_utility)
y3_100 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_100 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

#初始化设置 共80人
model = initialize.Model(5,16,80,5,3,100,1,5)
EC_choose = np.array(value_2.EC_choose)
EC_choose01 = np.zeros((model.group_num,model.num))

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.group_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

SES_utility,SES_choosed,group_SES = main(model,value_2.EC_choose,group_utility,value_2.SES_x_all,value_2.SES_x_res,value_2.SES_cost,value_2.SES_price1,SES_utility)
y1_80 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_80 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

SES_utility,SES_choosed,group_SES = main(model,value_2.EC_choose,group_utility,value_2.SES_x_all,value_2.SES_x_res,value_2.SES_cost,value_2.SES_price2,SES_utility)
y2_80 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_80 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

SES_utility,SES_choosed,group_SES = main(model,value_2.EC_choose,group_utility,value_2.SES_x_all,value_2.SES_x_res,value_2.SES_cost,value_2.SES_price3,SES_utility)
y3_80 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_80 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

#初始化设置 共60人
model = initialize.Model(5,12,60,5,3,100,1,5)
EC_choose = np.array(value_3.EC_choose)
EC_choose01 = np.zeros((model.group_num,model.num))

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.group_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

SES_utility,SES_choosed,group_SES = main(model,value_3.EC_choose,group_utility,value_3.SES_x_all,value_3.SES_x_res,value_3.SES_cost,value_3.SES_price1,SES_utility)
y1_60 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_60 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

SES_utility,SES_choosed,group_SES = main(model,value_3.EC_choose,group_utility,value_3.SES_x_all,value_3.SES_x_res,value_3.SES_cost,value_3.SES_price2,SES_utility)
y2_60 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_60 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

SES_utility,SES_choosed,group_SES = main(model,value_3.EC_choose,group_utility,value_3.SES_x_all,value_3.SES_x_res,value_3.SES_cost,value_3.SES_price3,SES_utility)
y3_60 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_60 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

#初始化设置 共40人
model = initialize.Model(5,8,40,5,3,100,1,5)
EC_choose = np.array(value_4.EC_choose)
EC_choose01 = np.zeros((model.group_num,model.num))

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.group_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

SES_utility,SES_choosed,group_SES = main(model,value_4.EC_choose,group_utility,value_4.SES_x_all,value_4.SES_x_res,value_4.SES_cost,value_4.SES_price1,SES_utility)
y1_40 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_40 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

SES_utility,SES_choosed,group_SES = main(model,value_4.EC_choose,group_utility,value_4.SES_x_all,value_4.SES_x_res,value_4.SES_cost,value_4.SES_price2,SES_utility)
y2_40 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_40 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

SES_utility,SES_choosed,group_SES = main(model,value_4.EC_choose,group_utility,value_4.SES_x_all,value_4.SES_x_res,value_4.SES_cost,value_4.SES_price3,SES_utility)
y3_40 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_40 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

#初始化设置 共25人
model = initialize.Model(5,5,25,5,3,100,1,5)
EC_choose01 = np.zeros((model.group_num,model.num))

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.group_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

SES_utility,SES_choosed,group_SES = main(model,value_5.EC_choose,group_utility,value_5.SES_x_all,value_5.SES_x_res,value_5.SES_cost,value_5.SES_price1,SES_utility)
y1_25 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_25 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

SES_utility,SES_choosed,group_SES = main(model,value_5.EC_choose,group_utility,value_5.SES_x_all,value_5.SES_x_res,value_5.SES_cost,value_5.SES_price2,SES_utility)
y2_25 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_25 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

SES_utility,SES_choosed,group_SES = main(model,value_5.EC_choose,group_utility,value_5.SES_x_all,value_5.SES_x_res,value_5.SES_cost,value_5.SES_price3,SES_utility)
y3_25 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_25 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 



x = np.array([25, 40, 60, 80, 100])  
y1 = np.array([y1_25[1],y1_40[1],y1_60[1],y1_80[1],y1_100[1]])
y2 = np.array([y2_25[1],y2_40[1],y2_60[1],y2_80[1],y2_100[1]])
y3 = np.array([y3_25[1],y3_40[1],y3_60[1],y3_80[1],y3_100[1]])

all1 = np.array([all1_25,all1_40,all1_60,all1_80,all1_100])
all2 = np.array([all2_25,all2_40,all2_60,all2_80,all2_100])
all3 = np.array([all3_25,all3_40,all3_60,all3_80,all3_100])


plt.figure(figsize = (7,7))
plt.plot(x,y1,'-*',linewidth=1.5)
plt.plot(x,y2,'-p',linewidth=1.5)
plt.plot(x,y3,'-+',linewidth=1.5)

plt.legend(['p2=0.45','p2=0.5','p2=0.57'],loc="best") # 把标签加载到图中哪个位

plt.xlabel('the number of ECs')
plt.ylabel('the utility of SES_2')

plt.show()

plt.figure(figsize = (7,7))
plt.plot(x,all1,'-*',linewidth=1.5)
plt.plot(x,all2,'-p',linewidth=1.5)
plt.plot(x,all3,'-+',linewidth=1.5)

plt.xlabel('the number of ECs')
plt.ylabel('the utility of all SESs')

plt.legend(['p2=0.45','p2=0.5','p2=0.57'],loc="best")

plt.show()


