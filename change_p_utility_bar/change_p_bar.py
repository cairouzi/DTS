import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
# from initialize import Model
from base_function.change_p_utility.main_220 import main_220
from base_function.change_p_utility.main_200 import main_200
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



"""#初始化设置 共200人
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
"""




#英文
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [y2_220[0], y2_220[1], y2_220[2], y2_220[3], y2_220[4]]
y3 = [y3_220[0], y3_220[1], y3_220[2], y3_220[3], y3_220[4]]

y1 = np.round(y1,5)
y2 = np.round(y2,5)
y3 = np.round(y3,5)

x_len = np.arange(len(x))
total_width, n = 0.9, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize=(10, 8))  

# axis取值可以为'both','x','y'， both是网格，x是只有垂直于x轴的线，y是只有垂直于yz轴的线
# c是设置线的颜色，linestyle 是画出的线的类型， zorder 是让线位于柱子下面而设置的，其值越小，线越靠下
plt.grid(axis="y", c='#d2c9eb', linestyle = '--', zorder = 0)
# 画第一个柱子，是批量画的，X轴的每个标签都开始画第一个柱子
# f1_1就是X轴所有标签对应的第一个柱子的y值
# width是设置柱子的宽度
# label就是图例
# color设置颜色
# edgecolor是设置柱子框的颜色
# linewidth是设置柱子框的线宽
# zorder 是保证柱子位于网格线的上方
plt.bar(xticks, y1, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, y2, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)

plt.bar(xticks + 2 * width, y3, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)

# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x, fontsize=35) 
plt.gca().tick_params(axis='both', labelsize=35)
plt.yticks(range(0, 50, 10),fontsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('the utility of SESs',fontsize = 35)  
plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize = 35) # 把标签加载到图中哪个位
plt.savefig("bar.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题





#中文
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [y2_220[0], y2_220[1], y2_220[2], y2_220[3], y2_220[4]]
y3 = [y3_220[0], y3_220[1], y3_220[2], y3_220[3], y3_220[4]]

y1 = np.round(y1,5)
y2 = np.round(y2,5)
y3 = np.round(y3,5)

x_len = np.arange(len(x))
total_width, n = 0.9, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize=(10, 8))  
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
plt.bar(xticks, y1, width=0.9*width,color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, y2, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)

plt.bar(xticks + 2 * width, y3, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)

# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 50, 10),fontsize=35)
plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('SES的净效用',fontsize = 35)  
plt.legend(['$p_2=0.40$','$p_2=0.45$','$p_2=0.50$'],loc="best",fontsize = 35) # 把标签加载到图中哪个位
plt.savefig("柱状图.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#中文
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [y2_220[0], y2_220[1], y2_220[2], y2_220[3], y2_220[4]]
y3 = [y3_220[0], y3_220[1], y3_220[2], y3_220[3], y3_220[4]]

y1 = np.round(y1,5)
y2 = np.round(y2,5)
y3 = np.round(y3,5)

x_len = np.arange(len(x))
total_width, n = 1.2, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize=(10, 8))   
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
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 50, 10),fontsize=35)
#plt.legend(['$p_2=0.50$'],loc="best",fontsize = 15) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('SES 的净效用',fontsize = 35)  
plt.savefig("柱状.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#英文
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [y2_220[0], y2_220[1], y2_220[2], y2_220[3], y2_220[4]]
y3 = [y3_220[0], y3_220[1], y3_220[2], y3_220[3], y3_220[4]]

y1 = np.round(y1,5)
y2 = np.round(y2,5)
y3 = np.round(y3,5)

x_len = np.arange(len(x))
total_width, n = 1.2, 3
width = total_width/n
# xticks 就是三个柱子的开始位置
xticks = x_len - (total_width - width) / 2

plt.figure(figsize=(10, 8))  
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
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 50, 10),fontsize=35)
#plt.legend(['$p_2=0.50$'],loc="best",fontsize = 15) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('the net utility of SES',fontsize = 35)  
plt.savefig("change_p bar.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题





plt.show()


