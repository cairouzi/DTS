import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from complexity_2 import complexity_2
from complexity_5 import complexity_5

# 或者使用其他支持中文的字体
# 设置中文字体为宋体, 英文标签使用新罗马字体
plt.rcParams['font.family'] = ['Times New Roman + SimSun']
# 解决负号'-'显示为方块的问题   
plt.rcParams['axes.unicode_minus'] = False  

# 分别设置mathtext公式的正体和斜体字体
plt.matplotlib.rcParams['mathtext.fontset'] = 'custom'
plt.matplotlib.rcParams['mathtext.rm'] = 'Times New Roman'  # 用于正常数学文本
plt.matplotlib.rcParams['mathtext.it'] = 'Times New Roman:italic'  # 用于斜体数学文本


# 设置运行参数
NUM_RUNS = 5  # 每组实验运行的次数

# 初始化存储结果的数组
iter_results_100_2 = np.zeros(NUM_RUNS)
iter_results_120_2 = np.zeros(NUM_RUNS)
iter_results_140_2 = np.zeros(NUM_RUNS)
iter_results_160_2 = np.zeros(NUM_RUNS)
iter_results_180_2 = np.zeros(NUM_RUNS)

# 初始化存储结果的数组
iter_results_100_5 = np.zeros(NUM_RUNS)
iter_results_120_5 = np.zeros(NUM_RUNS)
iter_results_140_5 = np.zeros(NUM_RUNS)
iter_results_160_5 = np.zeros(NUM_RUNS)
iter_results_180_5 = np.zeros(NUM_RUNS)

iter_results_100_2,iter_results_120_2,iter_results_140_2,iter_results_160_2,iter_results_180_2 = complexity_2()
iter_results_100_5,iter_results_120_5,iter_results_140_5,iter_results_160_5,iter_results_180_5 = complexity_5()

# 计算平均迭代次数
avg_iter_100_2 = np.mean(iter_results_100_2)
avg_iter_120_2 = np.mean(iter_results_120_2)
avg_iter_140_2 = np.mean(iter_results_140_2)
avg_iter_160_2 = np.mean(iter_results_160_2)
avg_iter_180_2 = np.mean(iter_results_180_2)

avg_iter_100_5 = np.mean(iter_results_100_5)
avg_iter_120_5 = np.mean(iter_results_120_5)
avg_iter_140_5 = np.mean(iter_results_140_5)
avg_iter_160_5 = np.mean(iter_results_160_5)
avg_iter_180_5 = np.mean(iter_results_180_5)

#图1中文
x = np.array([100, 120, 140, 160, 180])  

avg_iters_2 = np.array([avg_iter_100_2, avg_iter_120_2, avg_iter_140_2, avg_iter_160_2, avg_iter_180_2])
print("分为两组:", avg_iters_2)

avg_iters_5 = np.array([avg_iter_100_5, avg_iter_120_5, avg_iter_140_5, avg_iter_160_5, avg_iter_180_5])
print("分为两组:", avg_iters_5)

plt.figure(figsize = (10,8))


plt.plot(x, avg_iters_2, marker='p', color='#483D8B', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)

plt.plot(x, avg_iters_5, marker='p', color='orange', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)

plt.xlim(100, 180)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$H=2$','$H=5$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('ECs数量', fontsize=35)
plt.ylabel('迭代次数', fontsize=35)
plt.grid(linestyle='-.')

plt.savefig("复杂度.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

#图1英文
x = np.array([100, 120, 140, 160, 180])  


plt.figure(figsize = (10,8))

plt.plot(x, avg_iters_2, marker='p', color='#483D8B', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)

plt.plot(x, avg_iters_5, marker='p', color='orange', linestyle='-',
        markersize=20, linewidth=10, clip_on=False)


plt.xlim(100, 180)
plt.xticks(x, [str(val) for val in x],fontsize=35)
plt.yticks(fontsize=35)

plt.legend(['$H=2$','$H=5$'],loc="best",fontsize=35) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35) 
plt.xlabel('the number of ECs', fontsize=35)
plt.ylabel('number of iterations', fontsize=35)
plt.grid(linestyle='-.')
plt.savefig("Comeplexity.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


plt.show()


