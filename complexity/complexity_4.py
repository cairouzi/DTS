import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
from base_function.complexity.main_180 import main_180
from base_function.complexity.main_160 import main_160
from base_function.complexity.main_140 import main_140
from base_function.complexity.main_120 import main_120
from base_function.complexity.main_100 import main_100
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

#分组为4
#初始化设置 共180人
model = initialize.Model(4,45,180,5,3,100,0.38,4)
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
iter_180_4 = 0

EC_choose = [[3,5,2,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,5,3,3,2,4,5,2,1,4,1,1,5,2,1,4,1,1,4],
             [5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1],
             [1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,3,4,2,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3],
             [2,4,4,1,1,5,2,1,4,3,5,2,1,5,5,1,5,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res,iter_180_4 = main_180(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_180_4 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]


#初始化设置 共160人
model = initialize.Model(4,40,160,5,3,100,0.38,4)
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
iter_160_4 = 0

EC_choose = [[1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,4,5,1,1,4,5,3,1,5,2],
             [1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,4,5,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2],
             [1,4,4,5,5,5,3,5,1,1,4,3,3,1,4,5,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4],
             [1,1,5,2,1,4,4,5,1,1,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res,iter_160_4 = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_160_4 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]

#初始化设置 共140人
model = initialize.Model(4,35,140,5,3,100,0.38,4)
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
iter_140_4 = 0

EC_choose = [[1,2,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,1,3,4,5,5,2,1,4,4,1,1],
             [2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,1,3,4,5,3,3,2,4,4,1,1,2,5,2,1,4,4,5],
             [5,5,3,5,1,1,4,3,3,1,1,3,4,5,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5],
             [2,1,4,1,3,4,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,1,3,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res,iter_140_4 = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_140_4 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]

#初始化设置 共120人
model = initialize.Model(4,30,120,5,3,100,0.38,4)
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
iter_120_4 = 0

EC_choose = [[1,1,1,5,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,5,1,1,4,4,1],
             [1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,2,5,2,1,4],
             [4,5,5,5,3,5,1,1,4,3,3,1,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,5,4,4],
             [1,1,5,2,1,4,1,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res,iter_120_4 = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_120_4 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]

#初始化设置 共100人
model = initialize.Model(4,25,100,5,3,100,0.38,4)
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
iter_100_4 = 0

EC_choose = [[1,5,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,4,1,1,3,4],
             [5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,2,4,5],
             [5,5,3,5,1,1,4,3,3,1,2,3,5,1,1,4,3,3,2,2,4,5,1,3,3],
             [2,4,4,1,1,1,1,5,5,2,2,4,5,2,3,3,2,4,4,1,1,2,4,4,5]]
SES_utility,SES_choosed,group_SES,EC_x_res,iter_100_4 = main_100(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_100_4 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]


#图1中文
x = np.array([100, 120, 140, 160, 180])  

iter_4 = np.array([iter_100_4,iter_120_4,iter_140_4,iter_160_4,iter_180_4])
print("分为四组:", iter_4)

plt.figure(figsize = (10,8))


plt.plot(x, iter_4, marker='p', color='#483D8B', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)

plt.xlim(100, 180)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$H=4$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('ECs数量', fontsize=35)
plt.ylabel('迭代次数', fontsize=35)
plt.grid(linestyle='-.')

plt.savefig("复杂度_4.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图1英文
x = np.array([100, 120, 140, 160, 180])  


plt.figure(figsize = (10,8))

plt.plot(x, iter_4, marker='p', color='#483D8B', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)


plt.xlim(100, 180)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$H=4$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('the number of ECs', fontsize=35)
plt.ylabel('number of iterations', fontsize=35)
plt.grid(linestyle='-.')
plt.savefig("Comeplexity_4.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.show()


