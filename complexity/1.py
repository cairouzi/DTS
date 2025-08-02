import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')

# 或者使用其他支持中文的字体
# 设置中文字体为宋体, 英文标签使用新罗马字体
plt.rcParams['font.family'] = ['Times New Roman + SimSun']
# 解决负号'-'显示为方块的问题   
plt.rcParams['axes.unicode_minus'] = False  

# 分别设置mathtext公式的正体和斜体字体
plt.matplotlib.rcParams['mathtext.fontset'] = 'custom'
plt.matplotlib.rcParams['mathtext.rm'] = 'Times New Roman'  # 用于正常数学文本
plt.matplotlib.rcParams['mathtext.it'] = 'Times New Roman:italic'  # 用于斜体数学文本


#图1中文
x = np.array([100, 120, 140, 160, 180])  

iter_2 = np.array([60, 73, 160, 282, 1270])
print("分为两组:", iter_2)

iter_4 = np.array([21, 100, 477, 552, 1848])
print("分为四组:", iter_4)

plt.figure(figsize = (10,8))


plt.plot(x, iter_2, marker='p', color='#483D8B', linestyle='-',
        markersize=20, linewidth=6, clip_on=False)
plt.plot(x, iter_4, marker='>', color='orange', linestyle='--',
        markersize=20, linewidth=6, clip_on=False)

plt.xlim(100, 180)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$H=2$','$H=4$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('ECs数量', fontsize=35)
plt.ylabel('迭代次数', fontsize=35)
plt.grid(linestyle='-.')

plt.savefig("复杂度.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图1英文
x = np.array([100, 120, 140, 160, 180])  


plt.figure(figsize = (10,8))

plt.plot(x, iter_2, marker='p', color='#483D8B', linestyle='-',
        markersize=20, linewidth=6, clip_on=False)
plt.plot(x, iter_4, marker='>', color='orange', linestyle='--',
        markersize=20, linewidth=6, clip_on=False)


plt.xlim(100, 180)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$H=2$','$H=4$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('the number of ECs', fontsize=35)
plt.ylabel('number of iterations', fontsize=35)
plt.grid(linestyle='-.')
plt.savefig("Comeplexity.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.show()