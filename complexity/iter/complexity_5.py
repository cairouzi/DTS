import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.getcwd()+'/test_1')
from base_function import initialize
# from initialize import Model
from base_function.complexity.main_220 import main_220
from base_function.complexity.main_200 import main_200
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

# 设置运行参数
NUM_RUNS = 5  # 每组实验运行的次数

# 初始化存储结果的数组
iter_results_100 = np.zeros(NUM_RUNS)
iter_results_120 = np.zeros(NUM_RUNS)
iter_results_140 = np.zeros(NUM_RUNS)
iter_results_160 = np.zeros(NUM_RUNS)
iter_results_180 = np.zeros(NUM_RUNS)

#分组为5
def complexity_5():
        for i in (range(NUM_RUNS)):
                #初始化设置 共180人
                print("180循环",i)
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
                iter_180_5 = 0

                EC_choose = [[3,5,2,1,3,2,1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[1,1,5,2,1,4,1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,2,3,3,2,4,1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[3,4,2,3,5,1,1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4],[3,5,2,1,5,5,1,5,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
                SES_utility,SES_choosed,group_SES,EC_x_res,iter_180_5 = main_180(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
                y2_180_5 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
                iter_results_180[i] = iter_180_5

        for i in (range(NUM_RUNS)):
                #初始化设置 共160人
                print("160循环",i)
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
                iter_160_5 = 0

                EC_choose = [[1,1,4,5,3,1,2,1,3,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,4,5],[1,1,4,5,3,1,5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,4,5],[1,1,4,5,3,2,3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,4,5],[1,1,4,5,3,4,2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,4,5],[1,1,4,5,3,5,2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,4,5]]
                SES_utility,SES_choosed,group_SES,EC_x_res,iter_160_5 = main_160(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
                y2_160_5 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
                iter_results_160[i] = iter_160_5

        for i in (range(NUM_RUNS)):
                #初始化设置 共140人
                print("140循环",i)
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
                iter_140_5 = 0

                EC_choose = [[1,2,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4,1,3,4,5],[5,2,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2,1,3,4,5],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1,1,3,4,5],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,2,4,4,1,1,5,2,1,4,1,3,4,5],[2,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5,1,3,4,5]]
                SES_utility,SES_choosed,group_SES,EC_x_res,iter_140_5 = main_140(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
                y2_140_5 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
                iter_results_140[i] = iter_140_5

        for i in (range(NUM_RUNS)):
                #初始化设置 共120人
                print("120循环",i)
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
                iter_120_5 = 0

                EC_choose = [[1,1,1,5,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4,5,2,1,4],[5,1,1,4,4,1,1,2,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,5,2,1,4,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,2,3,3,5,4,4,1,1,5,2,1,4],[1,1,5,5,2,2,4,5,2,3,3,2,5,2,1,4,4,4,1,1,2,4,4,5]]
                SES_utility,SES_choosed,group_SES,EC_x_res,iter_120_5 = main_120(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
                y2_120_5 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
                iter_results_120[i] = iter_120_5

        for i in (range(NUM_RUNS)):
                #初始化设置 共100人
                print("100循环",i)
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
                iter_100_5 = 0

                EC_choose = [[1,5,1,2,3,5,1,1,4,3,4,2,2,4,5,2,3,3,2,4],[4,1,1,3,4,5,1,2,3,5,1,1,4,3,3,2,2,4,5,2],[3,3,2,4,4,1,1,2,4,5,5,5,3,5,1,1,4,3,3,1],[2,3,5,1,1,4,3,3,2,2,4,5,1,3,3,2,4,4,1,1],[1,1,5,5,2,2,4,5,2,3,3,2,4,4,1,1,2,4,4,5]]
                SES_utility,SES_choosed,group_SES,EC_x_res,iter_100_5 = main_100(model,EC_choose,group_utility,value.SES_x_all,value.SES_x_res,value.SES_cost,value.SES_price2,SES_utility)
                y2_100_5 = [SES_utility[0],SES_utility[1],SES_utility[2],SES_utility[3],SES_utility[4]]
                iter_results_100[i] = iter_100_5
        
        return iter_results_100,iter_results_120,iter_results_140,iter_results_160,iter_results_180
