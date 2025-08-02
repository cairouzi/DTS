import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
# from initialize import Model
from base_function.change_x_utility.main_160 import main_160
from base_function.change_x_utility.main_150 import main_150
from base_function.change_x_utility.main_140 import main_140
from base_function.change_x_utility.main_130 import main_130
from base_function.change_x_utility.main_120 import main_120
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
SES_utility,SES_choosed,group_SES,EC_x_res = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res1,value.SES_cost,value.SES_price1,SES_utility)
y1_120 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_120 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]


EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_130(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res2,value.SES_cost,value.SES_price1,SES_utility)
y1_130 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_130 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res3,value.SES_cost,value.SES_price1,SES_utility)
y1_140 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_140 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_150(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res4,value.SES_cost,value.SES_price1,SES_utility)
y1_150 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_150 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res5,value.SES_cost,value.SES_price1,SES_utility)
y1_160 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all1_160 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 



#price2
EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res1,value.SES_cost,value.SES_price2,SES_utility)
y2_120 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_120 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]


EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_130(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res2,value.SES_cost,value.SES_price2,SES_utility)
y2_130 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_130 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res3,value.SES_cost,value.SES_price2,SES_utility)
y2_140 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_140 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_150(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res4,value.SES_cost,value.SES_price2,SES_utility)
y2_150 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_150 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res5,value.SES_cost,value.SES_price2,SES_utility)
y2_160 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all2_160 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 


#price3
EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res1,value.SES_cost,value.SES_price3,SES_utility)
y3_120 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_120 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4]


EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_130(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res2,value.SES_cost,value.SES_price3,SES_utility)
y3_130 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_130 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res3,value.SES_cost,value.SES_price3,SES_utility)
y3_140 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_140 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_150(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res4,value.SES_cost,value.SES_price3,SES_utility)
y3_150 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_150 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 

EC_choose = [[1,1,4,5,5,1,1,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,4,5,3,1,5,5,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[1,1,4,5,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[1,1,4,5,3,4,3,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[1,1,4,5,3,5,2,1,5,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,5,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res5,value.SES_cost,value.SES_price3,SES_utility)
y3_160 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
all3_160 = SES_utility[0] + SES_utility[1] + SES_utility[2] + SES_utility[3] + SES_utility[4] 


#图1中文
x = np.array([120, 130, 140, 150, 160])  
y3 = np.array([y3_120[1],y3_130[1],y3_140[1],y3_150[1],y3_160[1]])

plt.figure(figsize = (10,8))

plt.plot(x, y3, marker='>', color='orange', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)

plt.xlim(120, 160)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(range(32, 43, 2),fontsize=35)

plt.legend(['$p_2=0.50$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('资源量', fontsize=35)
plt.ylabel('SES$_2$的净效用', fontsize=35)



plt.grid(linestyle='-.')

plt.savefig("不同资源下SES_2的效用的变化.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图1英文
plt.figure(figsize = (10,8))
x = np.array([120, 130, 140, 150, 160])  

plt.plot(x, y3, marker='>', color='orange', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)

plt.xlim(120, 160)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(range(32, 4, 2),fontsize=35)

plt.legend(['$p_2=0.50$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('electricity volume', fontsize=35)
plt.ylabel('the net utility of SES$_2$', fontsize=35)
plt.grid(linestyle='-.')
plt.savefig("Changes in the utility of SES_2 with different resources.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#图2中文
x = np.array([120, 130, 140, 150, 160])  

y1 = np.array([y1_120[1],y1_130[1],y1_140[1],y1_150[1],y1_160[1]])
y2 = np.array([y2_120[1],y2_130[1],y2_140[1],y2_150[1],y2_160[1]])
y3 = np.array([y3_120[1],y3_130[1],y3_140[1],y3_150[1],y3_160[1]])

plt.figure(figsize = (10,8))
plt.plot(x, y1, marker='p', color='red', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y2, marker='>', color='orange', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y3, marker='o', color='green', linestyle='-',
          markersize=20, linewidth=6, clip_on=False)

plt.xlim(120, 160)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('资源量', fontsize=35)
plt.ylabel('SES$_2$的净效用', fontsize=35)
plt.grid(linestyle='-.')

plt.savefig("不同资源和价格下SES_2的效用的变化.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图2英文
plt.figure(figsize = (10,8))
x = np.array([120, 130, 140, 150, 160])  

plt.plot(x, y1, marker='p', color='red', linestyle='-',
        markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y2, marker='>', color='orange', linestyle='-',
        markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y3, marker='o', color='green', linestyle='-',
        markersize=20, linewidth=6, clip_on=False)


plt.xlim(120, 160)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('electricity volume', fontsize=35)
plt.ylabel('the net utility of SES$_2$', fontsize=35)
plt.grid(linestyle='-.')
plt.savefig("Changes in the utility of SES_2 with different resources and price.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#图3中文
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y1 = [y1_160[0], y1_160[1], y1_160[2], y1_160[3], y1_160[4]]
y2 = [y2_160[0], y2_160[1], y2_160[2], y2_160[3], y2_160[4]]
y3 = [y3_160[0], y3_160[1], y3_160[2], y3_160[3], y3_160[4]]

y1 = np.round(y1,5)
y2 = np.round(y2,5)
y3 = np.round(y3,5)

x_len = np.arange(len(x))
total_width, n = 1.2, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize = (10,8))
# 这里定义ax，是为了后面画图的边框所用
# axis取值可以为'both','x','y'， both是网格，x是只有垂直于x轴的线，y是只有垂直于yz轴的线
# c是设置线的颜色，linestyle 是画出的线的类型， zorder 是让线位于柱子下面而设置的，其值越小，线越靠下
plt.grid(axis="y", c='#d2c9eb', linestyle = '--', zorder=0)
# 画第一个柱子，是批量画的，X轴的每个标签都开始画第一个柱子
# f1_1就是X轴所有标签对应的第一个柱子的y值
# width是设置柱子的宽度
# label就是图例
# color设置颜色
# edgecolor是设置柱子框的颜色
# linewidth是设置柱子框的线宽
# zorder 是保证柱子位于网格线的上方

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, y3, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x,fontsize=35) 
plt.yticks(range(0, 50, 10),fontsize=35)
plt.legend(['$x_2=160$'],loc="best",fontsize=35) # 把标签加载到图中哪个位


plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('SES的净效用',fontsize = 35)  
plt.savefig("改变资源量的柱状.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图3英文
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y1 = [y1_160[0], y1_160[1], y1_160[2], y1_160[3], y1_160[4]]
y2 = [y2_160[0], y2_160[1], y2_160[2], y2_160[3], y2_160[4]]
y3 = [y3_160[0], y3_160[1], y3_160[2], y3_160[3], y3_160[4]]

y1 = np.round(y1,5)
y2 = np.round(y2,5)
y3 = np.round(y3,5)

x_len = np.arange(len(x))
total_width, n = 1.2, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize = (10,8))
# 这里定义ax，是为了后面画图的边框所用
# axis取值可以为'both','x','y'， both是网格，x是只有垂直于x轴的线，y是只有垂直于yz轴的线
# c是设置线的颜色，linestyle 是画出的线的类型， zorder 是让线位于柱子下面而设置的，其值越小，线越靠下
plt.grid(axis="y", c='#d2c9eb', linestyle = '--', zorder=0)
# 画第一个柱子，是批量画的，X轴的每个标签都开始画第一个柱子
# f1_1就是X轴所有标签对应的第一个柱子的y值
# width是设置柱子的宽度
# label就是图例
# color设置颜色
# edgecolor是设置柱子框的颜色
# linewidth是设置柱子框的线宽
# zorder 是保证柱子位于网格线的上方

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, y3, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x,fontsize=35) 
plt.yticks(range(0, 50, 10),fontsize=35)
plt.legend(['$x_2=160$'],loc="best",fontsize=35) # 把标签加载到图中哪个位


plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('the net utility of SES',fontsize = 35)  
plt.savefig("bar Change in volume of resources.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#图4英文 三个柱状
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y_120 = [y3_120[0], y3_120[1], y3_120[2], y3_120[3], y3_120[4]]
y_140 = [y3_140[0], y3_140[1], y3_140[2], y3_140[3], y3_140[4]]
y_160 = [y3_160[0], y3_160[1], y3_160[2], y3_160[3], y3_160[4]]


x_len = np.arange(len(x))
total_width, n = 0.9, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize = (10,8)) 
# 这里定义ax，是为了后面画图的边框所用
# axis取值可以为'both','x','y'， both是网格，x是只有垂直于x轴的线，y是只有垂直于yz轴的线
# c是设置线的颜色，linestyle 是画出的线的类型， zorder 是让线位于柱子下面而设置的，其值越小，线越靠下
plt.grid(axis="y", c='#d2c9eb', linestyle = '--', zorder=0)
# 画第一个柱子，是批量画的，X轴的每个标签都开始画第一个柱子
# f1_1就是X轴所有标签对应的第一个柱子的y值
# width是设置柱子的宽度
# label就是图例
# color设置颜色
# edgecolor是设置柱子框的颜色
# linewidth是设置柱子框的线宽
# zorder 是保证柱子位于网格线的上方

plt.bar(xticks, y_120, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, y_140, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)

plt.bar(xticks + 2 * width, y_160, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
#plt.bar(xticks + width, y3, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x,fontsize=35) 
plt.yticks(range(0, 50, 10),fontsize=35)
plt.legend(['$x_2=120$', '$x_2=140$', '$x_2=160$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('the net utility of SES',fontsize = 35)  
plt.savefig("bar Change in electricity volume.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.show()


