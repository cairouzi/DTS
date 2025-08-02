import time
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize

from Comparative_experiment1.main_100 import main_100

from Comparative_experiment1.peer.Peer_and_Negotiator import PeerMatching
from Comparative_experiment1.peer.peer_initialize import Buyer, Seller

from Comparative_experiment1.game.coalition_graph_game import Game
from Comparative_experiment1.game.game_initialize import B, S

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

#对比

#原方法
#初始化设置 共100人
start_time_3 = time.time()  # 获取当前时间（秒为单位）
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
SES_utility,SES_choosed,group_SES,EC_x_res,SES_x_res = main_100(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price4,SES_utility)
y3 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]

energy_3 = [SES_x_res[0],SES_x_res[1],SES_x_res[2],SES_x_res[3],SES_x_res[4]]
for i in range(5):
        print(energy_3[i])
end_time_3 = time.time()  # 再次获取当前时间
elapsed_time_3 = end_time_3 - start_time_3  # 计算时间差

#对比方法1

# 示例输入 
start_time_2 = time.time()  # 获取当前时间（秒为单位） 
sellers = [Seller(8, 0.43, 0, 150), Seller(10, 0.5, 0, 150), Seller(5, 0.48, 0, 160), Seller(10, 0.49, 0, 155), Seller(9, 0.46, 0, 150)] 
buyers = [Buyer(4, 0.24, 2, 4), Buyer(5, 0.24, 2, 5), Buyer(8, 0.62, 5, 8), Buyer(5, 0.46, 1, 5),
Buyer(9, 0.49, 4, 9), Buyer(10, 0.37, 4, 10), Buyer(9, 0.61, 4, 9), Buyer(8, 0.47, 4, 8),
Buyer(8, 0.31, 2, 8), Buyer(13, 0.55, 5, 13), Buyer(8, 0.39, 3, 8), Buyer(8, 0.37, 4, 8),
Buyer(5, 0.24, 1, 5), Buyer(3, 0.35, 1, 3), Buyer(6, 0.29, 2, 6), Buyer(8, 0.54, 5, 8),
Buyer(7, 0.30, 2, 7), Buyer(10, 0.39, 5, 10), Buyer(8, 0.21, 1, 8), Buyer(10, 0.27, 3, 10),
Buyer(12, 0.38, 5, 12), Buyer(11, 0.27, 7, 11), Buyer(10, 0.35, 5, 10), Buyer(10, 0.21, 2, 10),
Buyer(10, 0.27, 6, 10), Buyer(8, 0.13, 1, 8), Buyer(7, 0.97, 2, 7), Buyer(8, 0.53, 2, 8),
Buyer(12, 0.38, 5, 12), Buyer(3, 0.25, 3, 8), Buyer(13, 0.91, 8, 13), Buyer(9, 0.72, 5, 9),
Buyer(5, 0.51, 2, 5), Buyer(7, 0.32, 2, 7), Buyer(7, 0.62, 3, 7), Buyer(9, 0.63, 5, 9),
Buyer(9, 0.29, 2, 9), Buyer(6, 0.21, 1, 6), Buyer(8, 0.22, 2, 8), Buyer(9, 0.52, 4, 9),
Buyer(5, 0.20, 1, 5), Buyer(9, 0.53, 4, 9), Buyer(6, 0.75, 2, 6), Buyer(7, 0.26, 1, 7),
Buyer(9, 0.21, 6, 9), Buyer(8, 0.24, 4, 8), Buyer(6, 0.76, 1, 6), Buyer(7, 0.36, 2, 7),
Buyer(9, 0.14, 5, 9), Buyer(9, 0.35, 5, 9), Buyer(8, 0.39, 1, 8), Buyer(9, 0.24, 2, 9),
Buyer(9, 0.22, 5, 9), Buyer(8, 0.29, 2, 8), Buyer(8, 0.21, 2, 8), Buyer(7, 0.27, 2, 7),
Buyer(8, 0.48, 5, 8), Buyer(9, 0.27, 5, 9), Buyer(9, 0.35, 5, 9), Buyer(8, 0.51, 2, 8),
Buyer(7, 0.17, 3, 7), Buyer(8, 0.23, 2, 8), Buyer(9, 0.27, 4, 9), Buyer(14, 0.53, 4, 10),
Buyer(8, 0.16, 5, 8), Buyer(10, 0.22, 3, 10), Buyer(5, 0.24, 1, 5), Buyer(8, 0.49, 1, 8),
Buyer(7, 0.27, 1, 7), Buyer(6, 0.39, 1, 6), Buyer(5, 0.35, 1, 5), Buyer(9, 0.39, 3, 9),
Buyer(9, 0.25, 1, 9), Buyer(7, 0.21, 2, 7), Buyer(4, 0.22, 1, 4), Buyer(5, 0.32, 1, 5),
Buyer(5, 0.25, 2, 5), Buyer(9, 0.43, 5, 9), Buyer(7, 0.41, 3, 7), Buyer(8, 0.24, 4, 8),
Buyer(8, 0.29, 3, 8), Buyer(8, 0.39, 4, 8), Buyer(10, 0.32, 4, 10), Buyer(9, 0.58, 2, 9),
Buyer(8, 0.42, 2, 8), Buyer(5, 0.39, 1, 5), Buyer(8, 0.21, 2, 8), Buyer(6, 0.52, 1, 6),
Buyer(7, 0.28, 3, 7), Buyer(7, 0.31, 1, 7), Buyer(7, 0.3, 3, 7), Buyer(7, 0.55, 3, 7),
Buyer(7, 0.36, 4, 7), Buyer(8, 0.84, 4, 8), Buyer(6, 0.2, 2, 6), Buyer(9, 0.56, 1, 9),
Buyer(5, 0.26, 3, 5), Buyer(8, 0.22, 5, 8), Buyer(7, 0.24, 1, 7), Buyer(5, 0.44, 2, 8)
]

tau = [ [0.53, 0.23, 0.25, 0.40, 0.16, 0.39, 0.42, 0.49, 0.42, 0.40,
        0.37, 0.48, 0.38, 0.34, 0.18, 0.21, 0.40, 0.20, 0.30, 0.37,
        0.36, 0.50, 0.27, 0.24, 0.22, 0.16, 0.48, 0.34, 0.24, 0.49,
        0.25, 0.41 ,0.39, 0.24, 0.31, 0.15, 0.40, 0.25, 0.29, 0.31, 
        0.26, 0.23, 0.20, 0.39, 0.40, 0.38, 0.41, 0.21, 0.21, 0.23,
        0.27, 0.46, 0.36, 0.40, 0.25, 0.23, 0.43, 0.26, 0.21, 0.30,
        0.19, 0.28, 0.36, 0.23, 0.46, 0.39, 0.34, 0.36, 0.13, 0.29,
        0.31, 0.30, 0.46, 0.30, 0.32, 0.49, 0.24, 0.15, 0.16, 0.33,
        0.32, 0.28, 0.51, 0.30, 0.42, 0.49, 0.30, 0.27 ,0.28 ,0.42,
        0.37, 0.20, 0.40, 0.38, 0.32, 0.34, 0.31, 0.21, 0.26, 0.35],
        [0.27, 0.46, 0.36, 0.40, 0.25, 0.23, 0.43, 0.26, 0.21, 0.30,
        0.19, 0.28, 0.36, 0.23, 0.46, 0.39, 0.34, 0.36, 0.13, 0.29,
        0.31, 0.30, 0.46, 0.30, 0.32, 0.49, 0.24, 0.15, 0.16, 0.33,
        0.32, 0.28, 0.51, 0.30, 0.42, 0.49, 0.30, 0.27 ,0.28 ,0.42,
        0.37, 0.20, 0.40, 0.38, 0.32, 0.34, 0.31, 0.21, 0.26, 0.35,
        0.53, 0.23, 0.25, 0.40, 0.16, 0.39, 0.42, 0.49, 0.42, 0.40,
        0.37, 0.48, 0.38, 0.34, 0.18, 0.21, 0.40, 0.20, 0.30, 0.37,
        0.36, 0.50, 0.27, 0.24, 0.22, 0.16, 0.48, 0.34, 0.24, 0.49,
        0.25, 0.41 ,0.39, 0.24, 0.31, 0.15, 0.40, 0.25, 0.29, 0.31, 
        0.26, 0.23, 0.20, 0.39, 0.40, 0.38, 0.41, 0.21, 0.21, 0.23],
        [0.24, 0.25, 0.22, 0.45, 0.26, 0.22, 0.21, 0.48, 0.35, 0.33,
        0.36, 0.37, 0.35, 0.38, 0.32, 0.32, 0.36, 0.29, 0.28, 0.32,
        0.43, 0.37, 0.13, 0.38, 0.41, 0.35, 0.29, 0.39, 0.46, 0.27,
        0.22, 0.24, 0.28, 0.43, 0.42, 0.44, 0.24, 0.28, 0.25, 0.38,
        0.35, 0.23, 0.11, 0.28, 0.13, 0.36, 0.45, 0.11, 0.47, 0.29,
        0.25, 0.46, 0.26, 0.38, 0.40, 0.39, 0.31, 0.23, 0.41, 0.19,
        0.48, 0.28, 0.41, 0.21, 0.24, 0.37, 0.25, 0.47, 0.14, 0.38,
        0.01, 0.49, 0.46, 0.44, 0.28, 0.26, 0.24, 0.22, 0.26, 0.27,
        0.28, 0.32, 0.31, 0.30, 0.23, 0.42, 0.23, 0.25, 0.33, 0.34,
        0.37, 0.31, 0.29, 0.36, 0.21, 0.22, 0.20, 0.31, 0.22, 0.23],
        [0.25, 0.46, 0.26, 0.38, 0.40, 0.39, 0.31, 0.23, 0.41, 0.19,
        0.48, 0.28, 0.41, 0.21, 0.24, 0.37, 0.25, 0.47, 0.14, 0.38,
        0.01, 0.49, 0.46, 0.44, 0.28, 0.26, 0.24, 0.22, 0.26, 0.27,
        0.28, 0.32, 0.31, 0.30, 0.23, 0.42, 0.23, 0.25, 0.33, 0.34,
        0.37, 0.31, 0.29, 0.36, 0.21, 0.22, 0.20, 0.31, 0.22, 0.23,
        0.24, 0.25, 0.22, 0.45, 0.26, 0.22, 0.21, 0.48, 0.35, 0.33,
        0.36, 0.37, 0.35, 0.38, 0.32, 0.32, 0.36, 0.29, 0.28, 0.32,
        0.43, 0.37, 0.13, 0.38, 0.41, 0.35, 0.29, 0.39, 0.46, 0.27,
        0.22, 0.24, 0.28, 0.43, 0.42, 0.44, 0.24, 0.28, 0.25, 0.38,
        0.35, 0.23, 0.11, 0.28, 0.13, 0.36, 0.45, 0.11, 0.47, 0.29],
        [0.19, 0.28, 0.22, 0.23, 0.42, 0.30, 0.48, 0.33, 0.38, 0.33,
        0.18, 0.42, 0.48, 0.15, 0.20, 0.38, 0.37, 0.25, 0.25, 0.27, 
        0.30, 0.40, 0.25, 0.40, 0.31, 0.31, 0.22, 0.23, 0.51, 0.41,
        0.32, 0.14, 0.51, 0.11, 0.52, 0.43, 0.56, 0.25, 0.33, 0.44,
        0.45, 0.51, 0.35, 0.38, 0.28, 0.46, 0.15, 0.47, 0.55, 0.15,
        0.19, 0.28, 0.22, 0.23, 0.42, 0.30, 0.48, 0.33, 0.38, 0.33,
        0.18, 0.42, 0.48, 0.15, 0.20, 0.38, 0.37, 0.25, 0.25, 0.27, 
        0.30, 0.40, 0.25, 0.19, 0.28, 0.22, 0.23, 0.42, 0.30, 0.48, 
        0.33, 0.38, 0.33, 0.18, 0.42, 0.48, 0.15, 0.20, 0.38, 0.37, 
        0.30, 0.40, 0.25, 0.30, 0.40, 0.25, 0.19, 0.28, 0.30, 0.40]]        # 交易延迟矩阵  

matches = [[0] * len(buyers) for _ in range(len(sellers))]  
negotiations = [[0] * len(buyers) for _ in range(len(sellers))]
A_S = [[0] * len(buyers) for _ in range(len(sellers))]  # 初始化卖家意向矩阵   
A_B = [[0] * len(sellers) for _ in range(len(buyers))] 
P_S = [[0] * len(buyers) for _ in range(len(sellers))] 
P_B = [[0] * len(sellers) for _ in range(len(buyers))]
lambda_S = [[0] * len(buyers) for _ in range(len(sellers))] 
lambda_B = [[0] * len(sellers) for _ in range(len(buyers))]  
U_S = [0 for _ in range(len(sellers))] 
U_B = [0 for _ in range(len(buyers))]  
R = 30  # 最大迭代次数  
alpha_S = [0.14, 0.14, 0.13, 0.12, 0.15]
beta_S = [0.071, 0.073, 0.071, 0.08, 0.05]
alpha_B = [0.021, 0.023, 0.021, 0.023, 0.027, 0.017, 0.010,  0.021, 0.020, 0.018,
            0.011, 0.029, 0.028, 0.028, 0.029, 0.012, 0.024, 0.027, 0.029, 0.014, 
            0.021, 0.013, 0.023, 0.021, 0.013, 0.012, 0.022, 0.028, 0.030, 0.018,
            0.015, 0.028, 0.013, 0.021, 0.029, 0.017, 0.027, 0.026, 0.026, 0.010,
            0.012, 0.028, 0.028, 0.023, 0.027, 0.021, 0.013, 0.015, 0.019, 0.016,
            0.011, 0.029, 0.028, 0.028, 0.029, 0.012, 0.024, 0.027, 0.029, 0.014, 
            0.021, 0.013, 0.023, 0.021, 0.013, 0.012, 0.022, 0.028, 0.030, 0.018,
            0.015, 0.028, 0.013, 0.021, 0.029, 0.017, 0.027, 0.026, 0.011, 0.029, 
            0.028, 0.028, 0.029, 0.012, 0.024, 0.027, 0.029, 0.014, 0.021, 0.013,
            0.012, 0.028, 0.028, 0.023, 0.027, 0.021, 0.013, 0.015, 0.019, 0.016]
beta_B = [2.95, 2.94, 2.93, 2.92, 2.91, 2.90, 2.96, 2.97, 2.92, 2.97, 
            2.96, 2.91, 2.93, 2.97, 2.94, 2.96, 2.97, 2.92, 2.91, 2.94,
            2.90, 2.97, 2.90, 2.98, 2.93, 2.94, 2.90, 2.98, 2.95, 2.97,
            2.90, 2.91, 2.93, 2.97, 2.99, 2.99, 2.91, 2.96, 2.92, 2.95,
            2.97, 2.98, 2.92, 2.96, 2.99, 2.93, 2.99, 2.94, 2.94, 2.92,
            2.90, 2.97, 2.90, 2.98, 2.93, 2.94, 2.90, 2.98, 2.95, 2.97,
            2.90, 2.91, 2.93, 2.97, 2.99, 2.99, 2.91, 2.96, 2.92, 2.95,
            2.97, 2.98, 2.92, 2.96, 2.99, 2.93, 2.99, 2.94, 2.94, 2.92,
            2.92, 2.94, 2.92, 2.94, 2.91, 2.93, 2.85, 2.94, 2.92, 2.97, 
            2.96, 2.91, 2.93, 2.97, 2.94, 2.96, 2.97, 2.92, 2.91, 2.94]
 
g_S = [0.09, 0.01, 0.09, 0.01, 0.01]
g_B = [0.05, 0.04, 0.07, 0.04, 0.09, 0.08, 0.07, 0.03, 0.03, 0.10,
        0.03, 0.04, 0.07, 0.10, 0.08, 0.03, 0.02, 0.04, 0.09, 0.06, 
        0.09, 0.02, 0.08, 0.02, 0.02, 0.09, 0.10, 0.10, 0.08, 0.01,
        0.09, 0.03, 0.10, 0.04, 0.06, 0.06, 0.10, 0.02, 0.07, 0.06, 
        0.08, 0.08, 0.04, 0.06, 0.06, 0.09, 0.07, 0.03, 0.08, 0.03,
        0.09, 0.03, 0.10, 0.04, 0.06, 0.06, 0.10, 0.02, 0.07, 0.06, 
        0.08, 0.08, 0.04, 0.06, 0.06, 0.09, 0.07, 0.03, 0.08, 0.03,
        0.09, 0.02, 0.08, 0.02, 0.02, 0.09, 0.10, 0.10, 0.08, 0.01,
        0.08, 0.08, 0.04, 0.06, 0.06, 0.09, 0.07, 0.03, 0.08, 0.03,
        0.05, 0.04, 0.07, 0.04, 0.09, 0.08, 0.07, 0.03, 0.03, 0.10,]

mu_lambda = 0.01
mu_g = 0.1
mu_p = 0.1
epsilon = 0.01
K = 30

energy_2 = []
#记录初始电力
for i in range(len(sellers)):
        energy_2.append(sellers[i].p)


# 运行匹配算法  
matching = PeerMatching(sellers, buyers, A_B, A_S, tau, matches, P_S, P_B, lambda_S, lambda_B, alpha_S, beta_S, alpha_B, beta_B, g_S, g_B, mu_lambda, mu_g, mu_p, epsilon, R, K, negotiations, U_S, U_B)
matches,U_S,U_B,negotiations = matching.run_matching()  
print(np.round(U_S,3))
print(np.round(U_B,3))

#电力（计算出售了多少电力）
for i in range(len(sellers)):
        energy_2[i] -= sellers[i].p

print(energy_2)


end_time_2 = time.time()  # 再次获取当前时间
elapsed_time_2 = end_time_2 - start_time_2  # 计算时间差




#对比方法2

# 示例输入 
start_time_1 = time.time()  # 获取当前时间（秒为单位） 
seller = {1: S(1, 150, 0.43, 0.22), 2: S(2, 150, 0.5, 0.25), 3: S(3, 160, 0.48, 0.30), 4: S(4, 155, 0.49, 0.23), 5: S(5, 150, 0.46, 0.24)} 
buyer = {1: B(1, 8, 0.43, 0.79), 2: B(2, 2, 0.16, 0.87), 3: B(3, 6, 0.61, 0.79), 4: B(4, 1, 0.54, 0.98),
5: B(5, 4, 0.4, 0.82), 6: B(6, 4, 0.12, 0.63), 7: B(7, 6, 0.62, 0.88), 8: B(8, 4, 0.57, 0.81), 
9: B(9, 7, 0.58, 0.99), 10: B(10, 4, 0.29, 0.55), 11: B(11, 5, 0.59, 0.87), 12: B(12, 3, 0.21, 0.87),
13: B(13, 10, 0.24, 0.55), 14: B(14, 10, 0.47, 0.65), 15: B(15, 5, 0.63, 0.98), 16: B(16, 6, 0.55, 0.99),
17: B(17, 4, 0.34, 0.82), 18: B(18, 4, 0.61, 0.97), 19: B(19, 6, 0.42, 0.64), 20: B(20, 2, 0.29, 0.51),
21: B(21, 7, 0.56, 0.77), 22: B(22, 3, 0.49, 0.73), 23: B(23, 8, 0.16, 0.98), 24: B(24, 10, 0.72, 0.99),
25: B(25, 3, 0.61, 0.81), 26: B(26, 5, 0.32, 0.92), 27: B(27, 7, 0.45, 0.88), 28: B(28, 2, 0.59, 0.93),
29: B(29, 8, 0.86, 0.92), 30: B(30, 7, 0.14, 0.49), 31: B(31, 6, 0.44, 0.78), 32: B(32, 1, 0.22, 0.52),
33: B(33, 2, 0.53, 0.89), 34: B(34, 7, 0.17, 0.91), 35: B(35, 7, 0.46, 0.7), 36: B(36, 2, 0.22, 0.5),
37: B(37, 9, 0.24, 0.44), 38: B(38, 5, 0.29, 0.79), 39: B(39, 2, 0.27, 0.92), 40: B(40, 7, 0.49, 0.87),
41: B(41, 7, 0.34, 0.92), 42: B(42, 3, 0.2, 0.83), 43: B(43, 6, 0.5, 0.85), 44: B(44, 8, 0.50, 0.91),
45: B(45, 8, 0.31, 0.49), 46: B(46, 10, 0.56, 0.88), 47: B(47, 10, 0.61, 0.94), 48: B(48, 9, 0.47, 0.96),
49: B(49, 6, 0.53, 0.74), 50: B(50, 9, 0.19, 0.4), 51: B(51, 4, 0.46, 0.66), 52: B(52, 10, 0.69, 0.81),
53: B(53, 10, 0.46, 0.62), 54: B(54, 7, 0.41, 0.74), 55: B(55, 3, 0.22, 0.54), 56: B(56, 10, 0.76, 0.94),
57: B(57, 4, 0.59, 0.72), 58: B(58, 9, 0.11, 0.31), 59: B(59, 1, 0.21, 0.78), 60: B(60, 2, 0.62, 0.86),
61: B(61, 1, 0.54, 0.68), 62: B(62, 3, 0.53, 0.94), 63: B(63, 1, 0.54, 0.72), 64: B(64, 4, 0.28, 0.43),
65: B(65, 9, 0.27, 0.38), 66: B(66, 5, 0.11, 0.5), 67: B(67, 7, 0.38, 0.99), 68: B(68, 3, 0.25, 0.88),
69: B(69, 7, 0.55, 0.97), 70: B(70, 3, 0.59, 0.93), 71: B(71, 1, 0.24, 0.99), 72: B(72, 9, 0.20, 0.6),
73: B(73, 7, 0.53, 0.84), 74: B(74, 3, 0.42, 0.95), 75: B(75, 8, 0.24, 0.72), 76: B(76, 6, 0.33, 0.61),
77: B(77, 3, 0.48, 0.98), 78: B(78, 8, 0.47, 0.97), 79: B(79, 5, 0.22, 0.75), 80: B(80, 1, 0.20, 0.48),
81: B(81, 5, 0.22, 0.55), 82: B(82, 1, 0.45, 0.77), 83: B(83, 4, 0.33, 0.99), 84: B(84, 9, 0.43, 0.93),
85: B(85, 5, 0.63, 0.94), 86: B(86, 10, 0.35, 0.56), 87: B(87, 9, 0.24, 0.65), 88: B(88, 4, 0.28, 0.61),
89: B(89, 7, 0.69, 0.99), 90: B(90, 7, 0.35, 0.82), 91: B(91, 9, 0.48, 0.99), 92: B(92, 9, 0.25, 0.75),
93: B(93, 6, 0.73, 0.95), 94: B(94, 9, 0.45, 0.72), 95: B(95, 1, 0.24, 0.64), 96: B(96, 4, 0.35, 0.95),
97: B(97, 8, 0.43, 0.85), 98: B(98, 6, 0.5, 0.61), 99: B(99, 5, 0.45, 0.98), 100: B(100, 9, 0.22, 0.74)}



# 初始化交易相关的数据结构
price = {}
coalitions = {}  # 使用字典来存储联盟信息，键可以是(seller_id, buyer_id)
benefit_S = {seller_id: 0 for seller_id in seller}
benefit_B = {buyer_id: 0 for buyer_id in buyer}

energy_1 = []
#记录初始电力
for key,value in seller.items():
        energy_1.append(value.energy)

#迭代次数
T = 30  

# 运行
game = Game(seller, buyer, T, price, coalitions, benefit_S, benefit_B)
coalitions, benefit_S, benefit_B = game.run()

#效用值
y1 = []
z1 = 0
for key, value in benefit_S.items():
        y1.append(np.round(value, 3))
        z1 += np.round(value, 3)
print(f"{key}: {y1}")

#电力（计算出售了多少电力）
for key,value in seller.items():
        energy_1[key - 1] -= value.energy

print(energy_1)


end_time_1 = time.time()  # 再次获取当前时间
elapsed_time_1 = end_time_1 - start_time_1  # 计算时间差


print(f"代码执行时间: {elapsed_time_3:.6f} 秒")
print(f"代码执行时间: {elapsed_time_2:.6f} 秒")
print(f"代码执行时间: {elapsed_time_1:.6f} 秒")


#中文  对比效用
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
#y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [U_S[0], U_S[1], U_S[2], U_S[3], U_S[4]]
y3 = [y3[0], y3[1], y3[2], y3[3], y3[4]]

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

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
#plt.bar(xticks + width, y3, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

plt.bar(xticks, y1, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, y2, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)

plt.bar(xticks + 2 * width, y3, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)



# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 60, 10),fontsize=35)

plt.legend(['Coalition graph game','Peer matching and negotiation','Proposed method'],loc="upper left",fontsize = 25) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('SES的净效用',fontsize = 35)  
plt.savefig("对比柱状.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#英文  对比效用
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
#y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [U_S[0], U_S[1], U_S[2], U_S[3], U_S[4]]
y3 = [y3[0], y3[1], y3[2], y3[3], y3[4]]

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

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
#plt.bar(xticks + width, y3, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)
plt.bar(xticks, y1, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)
plt.bar(xticks + width, y2, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)
plt.bar(xticks + 2 * width, y3, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)


# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 60, 10),fontsize=35)
plt.legend(['Coalition graph game','Peer matching and negotiation','Proposed method'],loc="upper left",fontsize = 25) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('the net utility of SES',fontsize = 35)  
plt.savefig("Comparative bar.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#中文  对比售卖的电力
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）

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

# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
#plt.bar(xticks + width, y3, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)

plt.bar(xticks, energy_1, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)
# xticks + width，表示的是X轴所有标签第二个柱子的起始位置
plt.bar(xticks + width, energy_2, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)
plt.bar(xticks + 2 * width, energy_3, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)



# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 200, 40),fontsize=35)

plt.legend(['Coalition graph game','Peer matching and negotiation','Proposed method'],loc="best",fontsize = 25) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 35) 
plt.ylabel('SES售卖的总电量',fontsize = 35)  
plt.savefig("对比电量柱状.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题


#英文  对比售卖的电力
# X轴标签
x = ['1','2','3','4','5']

# 这里是一个标签对应三个柱子，所以有三个数组（这实际上是不同模型在同一数据集上的的f1值对比）
#y1 = [y1_220[0], y1_220[1], y1_220[2], y1_220[3], y1_220[4]]
y2 = [U_S[0], U_S[1], U_S[2], U_S[3], U_S[4]]
y3 = [y3[0], y3[1], y3[2], y3[3], y3[4]]

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

plt.bar(xticks, energy_1, width=0.9*width, color="#a5dad2",edgecolor='white',linewidth = 0.5, zorder=2)
plt.bar(xticks + width, energy_2, width=0.9*width, color="#629286",edgecolor='white',linewidth = 0.5, zorder=2)
plt.bar(xticks + 2 * width, energy_3, width=0.9*width, color="#dae7b2",edgecolor='white',linewidth = 0.5, zorder=2)



# 设置x轴的刻度位置和标签  
plt.xticks(xticks + width, x, fontsize=35) 
plt.yticks(range(0, 200, 40),fontsize=35)
plt.legend(['Coalition graph game','Peer matching and negotiation','Proposed method'],loc="best",fontsize = 25) # 把标签加载到图中哪个位

plt.gca().tick_params(axis='both', labelsize=35)
plt.xlabel('SES',fontsize = 15) 
plt.ylabel('the total electricity volume sold by SES',fontsize = 35)  
plt.savefig("Comparative electricity volume bar.png", dpi=500, bbox_inches='tight')    # 解决图片不清晰，不完整的问题

plt.show()
