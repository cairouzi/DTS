import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
# from initialize import Model
from base_function.main import main
from base_function.change_p_num.main140 import main140
from base_function.change_p_num.main80 import main80
from base_function.change_p_num.main60 import main60

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



#初始化设置 共140人 1组70人
model = initialize.Model(2,70,140,2,3,100,0.4,5)

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_choose01 = np.zeros((model.group_num,model.num))
EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.SES_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

EC_choose = [[1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[2,2,2,2,2,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]
SES_utility,SES_choosed,group_SES,EC_x_res = main140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_70_0 = SES_choosed[0]
y1_70_1 = SES_choosed[1]


EC_choose = [[1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[2,2,2,2,2,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]
SES_utility,SES_choosed,group_SES,EC_x_res = main140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_70_0 = SES_choosed[0]
y2_70_1 = SES_choosed[1]

#初始化设置 共120人 1组60人
model = initialize.Model(2,60,120,2,3,100,0.4,5)

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_choose01 = np.zeros((model.group_num,model.num))
EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.SES_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

EC_choose = [[1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[1,2,1,2,1,1,2,1,2,1,1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]
SES_utility,SES_choosed,group_SES,EC_x_res = main(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_60_0 = SES_choosed[0]
y1_60_1 = SES_choosed[1]

EC_choose = [[1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[1,2,1,2,1,1,2,1,2,1,1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]
SES_utility,SES_choosed,group_SES,EC_x_res = main(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_60_0 = SES_choosed[0]
y2_60_1 = SES_choosed[1]




#初始化设置 共100人 1组50人
model = initialize.Model(2,50,100,2,3,100,0.4,5)

SES_choosed = np.zeros(model.SES_num)
SES_utility = np.zeros(model.SES_num)
SES_utility01 = np.zeros(model.SES_num)

EC_choose01 = np.zeros((model.group_num,model.num))
EC_SES_utility = np.zeros((model.group_num,model.num))
EC_transition = np.zeros((model.group_num,model.num))

group_SES = np.zeros((model.group_num, model.SES_num))
group_utility = np.zeros(model.group_num)
group_utility01 = np.zeros(model.group_num)
group_aver_u = np.zeros(model.group_num)

EC_choose = [[2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]
SES_utility,SES_choosed,group_SES,EC_x_res = main(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_50_0 = SES_choosed[0]
y1_50_1 = SES_choosed[1]

EC_choose = [[2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]
SES_utility,SES_choosed,group_SES,EC_x_res = main(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_50_0 = SES_choosed[0]
y2_50_1 = SES_choosed[1]


#初始化设置 共80人 1组40人
model = initialize.Model(2,40,80,2,3,100,0.4,5)
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

EC_choose = [[1,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1],[1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1]]
SES_utility,SES_choosed,group_SES,EC_x_res = main80(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_40_0 = SES_choosed[0]
y1_40_1 = SES_choosed[1]

EC_choose = [[1,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1],[1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1]]
SES_utility,SES_choosed,group_SES,EC_x_res = main80(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_40_0 = SES_choosed[0]
y2_40_1 = SES_choosed[1]



#初始化设置 共60人 1组30人
model = initialize.Model(2,30,60,2,3,100,0.38,4)
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

EC_choose = [[1,2,2,1,1,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1],[1,1,2,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1]]
SES_utility,SES_choosed,group_SES,EC_x_res = main60(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price1,SES_utility)
y1_30_0 = SES_choosed[0]
y1_30_1 = SES_choosed[1]


EC_choose = [[1,2,2,1,1,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1],[1,1,2,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1]]
SES_utility,SES_choosed,group_SES,EC_x_res = main60(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
y2_30_0 = SES_choosed[0]
y2_30_1 = SES_choosed[1]



#英文
x = np.array([30, 40, 50, 60, 70])  
y1_0 = np.array([y1_30_0,y1_40_0,y1_50_0,y1_60_0,y1_70_0])
y1_1 = np.array([y1_30_1,y1_40_1,y1_50_1,y1_60_1,y1_70_1])
y2_0 = np.array([y2_30_0,y2_40_0,y2_50_0,y2_60_0,y2_70_0])
y2_1 = np.array([y2_30_1,y2_40_1,y2_50_1,y2_60_1,y2_70_1])

plt.figure(figsize = (10,8))

plt.plot(x, y1_0, marker='p', color='#483D8B', linestyle='-',
        label=r'$k_1$', markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y1_1, marker='>', color='orange', linestyle='--',
        label=r'$k_2$', markersize=20, linewidth=6, clip_on=False)

plt.legend(loc="best", fontsize=35) # 把标签加载到图中哪个位

plt.xlim(30, 70)
plt.xticks(x, [str(val) for val in x])

# 设置x轴和y轴的标签，使用LaTeX语法添加下标  
plt.gca().tick_params(axis='both', labelsize=35) 

plt.xlabel('the number of ECs in group 2 $k^{(2)}$', fontsize=35)
plt.ylabel('the number of ECs \n choosing different SESs', fontsize=35)
plt.grid(linestyle='-.')     # 添加网格
plt.savefig("Adaptation of evolutionary equilibrium under different numbers of secondary users(p2=0.4).png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.figure(figsize = (10,8))
plt.plot(x, y2_0, marker='p', color='#483D8B', linestyle='-',
        label=r'$k_1$', markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y2_1, marker='>', color='orange', linestyle='--',
        label=r'$k_2$', markersize=20, linewidth=6, clip_on=False)

plt.legend(loc="best", fontsize=35) # 把标签加载到图中哪个位

plt.xlim(30, 70)
plt.xticks(x, [str(val) for val in x])

# 设置x轴和y轴的标签，使用LaTeX语法添加下标  
plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('the number of ECs in group 2 $k^{(2)}$', fontsize=35)
plt.ylabel('the number of ECs \n choosing different SESs', fontsize=35)
plt.grid(linestyle='-.')     # 添加网格
plt.savefig("Adaptation of evolutionary equilibrium under different numbers of secondary users(p2=0.6).png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#中文
x = np.array([30, 40, 50, 60, 70])  
y1_0 = np.array([y1_30_0,y1_40_0,y1_50_0,y1_60_0,y1_70_0])
y1_1 = np.array([y1_30_1,y1_40_1,y1_50_1,y1_60_1,y1_70_1])
y2_0 = np.array([y2_30_0,y2_40_0,y2_50_0,y2_60_0,y2_70_0])
y2_1 = np.array([y2_30_1,y2_40_1,y2_50_1,y2_60_1,y2_70_1])

plt.figure(figsize = (10,8))

plt.plot(x, y1_0, marker='p', color='#483D8B', linestyle='-',
        label=r'$k_1$', markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y1_1, marker='>', color='orange', linestyle='--',
        label=r'$k_2$', markersize=20, linewidth=6, clip_on=False)

plt.xlim(30, 70)
plt.xticks(x, [str(val) for val in x])

plt.legend(loc="best", fontsize=35) # 把标签加载到图中哪个位

# 设置x轴和y轴的标签，使用LaTeX语法添加下标  
plt.gca().tick_params(axis='both', labelsize=35) 

plt.xlabel('组2的 ECs 数量 $k^{(2)}$', fontsize=35)
plt.ylabel('选择不同SESs的\nECs数量', fontsize=35)
plt.grid(linestyle='-.')     # 添加网格
plt.savefig("不同次级用户数量下进化平衡的适应性(p2=0.4).png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.figure(figsize = (10,8))

plt.plot(x, y2_0, marker='p', color='#483D8B', linestyle='-',
        label=r'$k_1$', markersize=20, linewidth=6, clip_on=False)
plt.plot(x, y2_1, marker='>', color='orange', linestyle='--',
        label=r'$k_2$', markersize=20, linewidth=6, clip_on=False)

plt.legend(loc="best", fontsize=35) # 把标签加载到图中哪个位

plt.xlim(30, 70)
plt.xticks(x, [str(val) for val in x])
# 设置x轴和y轴的标签，使用LaTeX语法添加下标  
plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('组2的ECs数量 $k^{(2)}$', fontsize=35)
plt.ylabel('选择不同SESs的\nECs数量', fontsize=35)
plt.grid(linestyle='-.')     # 添加网格
plt.savefig("不同次级用户数量下进化平衡的适应性(p2=0.6).png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题



plt.show()


