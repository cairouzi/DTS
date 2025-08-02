import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.getcwd()+'/test_1')


from base_function import initialize
from base_function.complexity.group2.main import main

import value


# 或者使用其他支持中文的字体
# 设置中文字体为宋体, 英文标签使用新罗马字体
plt.rcParams['font.family'] = ['Times New Roman + SimSun']
# 解决负号'-'显示为方块的问题   
plt.rcParams['axes.unicode_minus'] = False  

# 分别设置mathtext公式的正体和斜体字体
plt.matplotlib.rcParams['mathtext.fontset'] = 'custom'
plt.matplotlib.rcParams['mathtext.rm'] = 'Times New Roman'  # 用于正常数学文本

import numpy as np
from scipy import stats

# 初始化模型和数据结构
model = initialize.Model(2,50,100,2,3,100,0.4,5)

# 实验重复次数
num_repeats = 1000

# 存储结果
results = np.zeros((num_repeats, model.SES_num))  # 存储每次实验的效用值

# 固定参数设置
EC_choose = [[1,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[1,2,2,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1,2,2,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1,2,2,2]]


# 重复实验
for i in range(num_repeats):
    # 每次实验重新初始化相关数组
    SES_choosed = np.zeros(model.SES_num)
    SES_utility = np.zeros(model.SES_num)
    group_utility = np.zeros(model.group_num)
    
    # 运行主实验
    SES_utility,SES_choosed,group_SES,EC_x_res = main(
        model, EC_choose, group_utility, 
        value.SES_x_all, value.SES_x_res, 
        value.SES_cost, value.SES_price2, SES_utility
    )
    
    # 存储结果
    results[i] = SES_utility

# 计算统计量函数
def calculate_stats(data):
    """计算所需的统计量"""
    stats_dict = {
        'mean': np.mean(data, axis=0),
        'std': np.std(data, axis=0, ddof=1),  # 样本标准差
        'variance': np.var(data, axis=0, ddof=1),  # 样本方差
        'range': np.ptp(data, axis=0),  # 极差 (max-min)
        'CI_low': np.zeros(data.shape[1]),
        'CI_high': np.zeros(data.shape[1])
    }
    
    n = len(data)
    for j in range(data.shape[1]):
        se = stats_dict['std'][j] / np.sqrt(n)  # 标准误
        stats_dict['CI_low'][j], stats_dict['CI_high'][j] = stats.t.interval(
            0.95, df=n-1, loc=stats_dict['mean'][j], scale=se)
    
    return stats_dict

# 计算统计量
stats_results = calculate_stats(results)

# 打印结果
print("="*60)
print("各SES组统计结果:")
print("="*60)
for group in range(model.SES_num):
    print(f"\nSES组 {group+1}:")
    print(f"  均值: {stats_results['mean'][group]:.4f}")
    print(f"  标准差: {stats_results['std'][group]:.4f}")
    print(f"  方差: {stats_results['variance'][group]:.4f}")
    print(f"  极差: {stats_results['range'][group]:.4f}")
    print(f"  95%置信区间: ({stats_results['CI_low'][group]:.4f}, {stats_results['CI_high'][group]:.4f})")

# 计算总效用统计量
total_utils = np.sum(results, axis=1)
total_stats = calculate_stats(total_utils.reshape(-1, 1))

print("\n" + "="*60)
print("总效用统计结果:")
print("="*60)
print(f"  均值: {total_stats['mean'][0]:.4f}")
print(f"  标准差: {total_stats['std'][0]:.4f}")
print(f"  方差: {total_stats['variance'][0]:.4f}")
print(f"  极差: {total_stats['range'][0]:.4f}")
print(f"  95%置信区间: ({total_stats['CI_low'][0]:.4f}, {total_stats['CI_high'][0]:.4f})")
print("="*60)

# 可选：保存结果到文件
np.savez('experiment_results.npz',
         group_utilities=results,
         total_utilities=total_utils,
         statistics=stats_results)
