import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
# from initialize import Model
from base_function.change_p_utility.main_220 import main_220
from base_function.change_p_utility.main_200 import main_200
from base_function.change_p_utility.main_180 import main_180
from base_function.change_p_utility.main_160 import main_160
from base_function.change_p_utility.main_140 import main_140
from base_function.change_p_utility.main_120 import main_120
from base_function.change_p_utility.main_100 import main_100
from base_function.main import main
import value

# 或者使用其他支持中文的字体
# 设置中文字体为宋体, 英文标签使用新罗马字体
plt.rcParams['font.family'] = ['Times New Roman + SimSun']
# 解决负号'-'显示为方块的问题   
plt.rcParams['axes.unicode_minus'] = False  

# 分别设置mathtext公式的正体和斜体字体
plt.matplotlib.rcParams['mathtext.fontset'] = 'custom'
plt.matplotlib.rcParams['mathtext.rm'] = 'Times New Roman'  # 用于正常数学文本
plt.matplotlib.rcParams['mathtext.it'] = 'Times New Roman:italic'  # 用于斜体数学文本


#初始化设置 共220人
model = initialize.Model(5,44,220,5,3,100,0.38,4)
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

EC_choose = [[1,1,4,5,1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_220(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_220 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_220 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,1,4,5,1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_220(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_220 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_220 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,1,4,5,1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_220(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_220 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_220 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]



#初始化设置 共200人
model = initialize.Model(5,40,200,5,3,100,0.38,4)
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

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_200(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_200 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_200 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_200(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_200 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_200 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_200(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_200 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_200 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 


#初始化设置 共180人
model = initialize.Model(5,36,180,5,3,100,0.38,4)
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

EC_choose = [[3,5,2,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,5,2,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[3,4,2,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[3,5,2,1,5,5,1,5,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_180(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_180 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_180 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[3,5,2,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,5,2,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[3,4,2,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[3,5,2,1,5,5,1,5,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_180(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_180 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_180 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[3,5,2,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,5,2,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[3,4,2,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[3,5,2,1,5,5,1,5,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_180(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_180 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_180 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 


#初始化设置 共160人
model = initialize.Model(5,32,160,5,3,100,0.38,4)
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

EC_choose = [[1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,4,5],[1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,4,5],[1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,4,5],[1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,4,5],[1,1,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_160 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_160 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,4,5],[1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,4,5],[1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,4,5],[1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,4,5],[1,1,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_160 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_160 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,4,5],[1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,4,5],[1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,4,5],[1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,4,5],[1,1,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_160 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_160 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 


#初始化设置 共140人
model = initialize.Model(5,28,140,5,3,100,0.38,4)
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

EC_choose = [[1,2,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,1,3,4,5],[5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,1,3,4,5],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,1,3,4,5],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,1,3,4,5],[2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,1,3,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_140 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_140 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,2,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,1,3,4,5],[5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,1,3,4,5],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,1,3,4,5],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,1,3,4,5],[2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,1,3,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_140 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_140 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,2,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,1,3,4,5],[5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,1,3,4,5],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,1,3,4,5],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,1,3,4,5],[2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,1,3,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_140 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_140 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 



#初始化设置 共120人
model = initialize.Model(5,24,120,5,3,100,0.38,4)
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

EC_choose = [[1,1,1,5,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[5,1,1,4,4,1,1,1,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,5,4,4,1,1,5,2,1,4],[1,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_120 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_120 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,1,1,5,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[5,1,1,4,4,1,1,1,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,5,4,4,1,1,5,2,1,4],[1,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_120 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_120 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,1,5,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[5,1,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,5,4,4,1,1,5,2,1,4],[1,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_120 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_120 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 




#初始化设置 共100人
model = initialize.Model(5,20,100,5,3,100,0.38,4)
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

EC_choose = [[1,5,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4],[4,1,1,3,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,1,3,3,2,4,4,1,1],[1,1,5,5,2,2,4,5,2,3,3,2,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_100(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_100 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_100 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]

EC_choose = [[1,5,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4],[4,1,1,3,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,1,3,3,2,4,4,1,1],[1,1,5,5,2,2,4,5,2,3,3,2,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_100(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_100 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_100 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,5,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4],[4,1,1,3,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,1,3,3,2,4,4,1,1],[1,1,5,5,2,2,4,5,2,3,3,2,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_100(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price3,SES_utility)
y3_100 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_100 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

print(y1_100[1] - y1_200[1])
print(y2_100[1] - y2_200[1])
print(y3_100[1] - y3_200[1])


print(y1_100[1] - y1_180[1])
print(y2_100[1] - y2_180[1])
print(y3_100[1] - y3_180[1])

#图1中文
x = np.array([100, 120, 140, 160, 180, 200, 220])  

y1_2 = np.array([y1_100[1],y1_120[1],y1_140[1],y1_160[1],y1_180[1],y1_200[1],y1_220[1]])
y2_2 = np.array([y2_100[1],y2_120[1],y2_140[1],y2_160[1],y2_180[1],y2_200[1],y2_220[1]])
y3_2 = np.array([y3_100[1],y3_120[1],y3_140[1],y3_160[1],y3_180[1],y3_200[1],y3_220[1]])


plt.figure(figsize = (10,8))
plt.plot(x, y1_2, marker='p', color='red', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y2_2, marker='>', color='orange', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y3_2, marker='o', color='green', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)

plt.xlim(100, 220)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(range(22, 42, 3),fontsize=35)

plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('ECs数量', fontsize=35)
plt.ylabel('SES$_2$的净效用', fontsize=35)
plt.grid(linestyle='-.')

plt.savefig("不同价格下SES_2的效用与EC数量的对比.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图1英文
x = np.array([100, 120, 140, 160, 180, 200, 220])  

y1_2 = np.array([y1_100[1],y1_120[1],y1_140[1],y1_160[1],y1_180[1],y1_200[1],y1_220[1]])
y2_2 = np.array([y2_100[1],y2_120[1],y2_140[1],y2_160[1],y2_180[1],y2_200[1],y2_220[1]])
y3_2 = np.array([y3_100[1],y3_120[1],y3_140[1],y3_160[1],y3_180[1],y3_200[1],y3_220[1]])


plt.figure(figsize = (10,8))
plt.plot(x, y1_2, marker='p', color='red', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y2_2, marker='>', color='orange', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y3_2, marker='o', color='green', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)

plt.xlim(100, 220)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(range(22, 42, 3),fontsize=35)

plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('the number of ECs', fontsize=35)
plt.ylabel('the net utility of SES$_2$', fontsize=35)
plt.grid(linestyle='-.')
plt.savefig("Utility of ECS 2 vs. the number of ECs for different prices.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#图2中文
all1 = np.array([all1_100,all1_120,all1_140,all1_160,all1_180,all1_200,all1_220])
all2 = np.array([all2_100,all2_120,all2_140,all2_160,all2_180,all2_200,all2_220])
all3 = np.array([all3_100,all3_120,all3_140,all2_160,all3_180,all3_200,all3_220])

plt.figure(figsize = (10,8))
plt.plot(x, all1, marker='p', color='red', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, all2, marker='>', color='orange', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, all3, marker='o', color='green', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)

plt.xlim(100, 220)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('ECs数量', fontsize=35)
plt.ylabel('所有SES的净效用', fontsize=35)
plt.grid(linestyle='-.')
plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize=35)
plt.savefig("不同EC数量下,价格对所有SES效用的影响.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图2英文
all1 = np.array([all1_100,all1_120,all1_140,all1_160,all1_180,all1_200,all1_220])
all2 = np.array([all2_100,all2_120,all2_140,all2_160,all2_180,all2_200,all2_220])
all3 = np.array([all3_100,all3_120,all3_140,all2_160,all3_180,all3_200,all3_220])


plt.figure(figsize = (10,8))
plt.plot(x, all1, marker='p', color='red', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, all2, marker='>', color='orange', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, all3, marker='o', color='green', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)

plt.xlim(100, 220)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('the number of ECs', fontsize=35)
plt.ylabel('the net utility of all SESs', fontsize=35)
plt.grid(linestyle='-.')
plt.legend(['$p_2=0.4$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize=35)
plt.savefig("The effect of price on SESs’ utilities for different number of ECs.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.show()


