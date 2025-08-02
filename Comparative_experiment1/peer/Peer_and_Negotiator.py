
import random
import numpy as np


class PeerMatching():

    def __init__(self, sellers, buyers, A_B, A_S, tau,  matches, P_S, P_B, lambda_S, lambda_B, alpha_S, beta_S, alpha_B, beta_B, g_S, g_B, mu_lambda, mu_g, mu_p, epsilon, R, K, negotiations, U_S, U_B):
        self.sellers = sellers              # 卖家列表，每个卖家有属性 pi, lambda_i, p_, p 
        self.buyers = buyers                # 买家列表，每个买家有属性 pj, lambda_j, p_, p  
        self.A_B = A_B                      # 买家意向矩阵，初始化为None  
        self.A_S = A_S                      # 卖家意向矩阵，初始化为None 
        self.tau = tau                      # 交易费用
        self.matches = matches              # 存储匹配结果 
        self.P_S = P_S                      # 卖家报价(电量)
        self.P_B = P_B                      # 买家报价(电量)
        self.lambda_S = lambda_S            # 卖家报价(价格)
        self.lambda_B = lambda_B            # 买家报价(价格)
        self.alpha_S = alpha_S              # 卖家价格调整系数1
        self.beta_S = beta_S                # 卖家价格调整系数2
        self.alpha_B = alpha_B              # 买家价格调整系数1
        self.beta_B = beta_B                # 买家价格调整系数2
        self.g_S = g_S                      # 卖家贪婪系数
        self.g_B = g_B                      # 买家贪婪系数     
        self.mu_lambda = mu_lambda          # 价格调整系数
        self.mu_g = mu_g                    # 贪婪调整系数
        self.mu_p = mu_p                    # 电量调整系数
        self.epsilon = epsilon              # 容差
        self.R = R                          # 最大匹配轮次
        self.K = K                          # 最大谈判轮次
        self.negotiations = negotiations    # 存储协商结果
        self.U_S = U_S                      # 存储卖家效用
        self.U_B = U_B                      # 存储买家效用


    #匹配过程
    def run_matching(self):   
        Ns = range(len(self.sellers)) 
        Nb = range(len(self.buyers)) 
        r = 1
        Match = 0
        matched_b_indices = set()  # 用于跟踪已经匹配的买家原始索引  
        while r <= self.R:  
            matched_s_indices = set()  # 用于跟踪已经匹配的卖家原始索引
            for i in Ns:  
                if self.sellers[i].p <= 0 :
                    continue  
                else:
                    unmatch_b_indeces = [j for j in Nb if j not in matched_b_indices]
                    sorted_buyers = sorted(unmatch_b_indeces, key=lambda j: self.buyers[j].lambda_j - self.tau[i][j], reverse=True)  
                    for j in sorted_buyers:  # 这里 j_index 是排序后的买家原始索引
                        # 检查这个买家是否已经被匹配过（使用原始索引）
                        if j in matched_b_indices:
                            continue  # 如果已经匹配，则跳过当前迭代
                        #判断是否可以选择这个Buyers
                        if self.sellers[i].pi >= self.buyers[j].pj and self.buyers[j].p > 0 :  
                            self.A_S[i][j] = 1  
                        else:  
                            self.A_S[i][j] = 0  

                        #判断是否双向
                        if self.A_S[i][j] == 1 and self.A_B[j][i] == 1:  
                            Match = 1
                            self.matches[i][j] = 1 
                            matched_b_indices.add(j)  # 将买家原始索引标记为已匹配
                            self.negotiations = self.negotiate(i,j)
                            if self.negotiations[i][j] == 1:   #协商成功，i j 重新加入匹配
                                print("匹配轮：",r)
                                break    
            if not Match:  
                for j in Nb:  
                    if self.buyers[j].p <= 0 or j in matched_b_indices:
                        continue                      
                    else:
                        sorted_sellers = sorted(Ns, key=lambda i: self.sellers[i].lambda_i - self.tau[i][j])  
                        for i in sorted_sellers:  
                            # 检查这个买家是否已经被匹配过（使用原始索引）
                            if i in matched_s_indices:
                                continue  # 如果已经匹配，则跳过当前迭代
                            #判断是否可以选择这个sellers
                            if self.buyers[j].pj <= self.sellers[i].pi and self.sellers[i].p > 0:  
                                self.A_B[j][i] = 1  
                            else:  
                                self.A_B[j][i] = 0  
                            #判断是否双向
                            if self.A_B[j][i] == 1 and self.A_S[i][j] == 1:  
                                Match = 1
                                self.matches[i][j] = 1
                                matched_s_indices.add(i)  # 将买家原始索引标记为已匹配
                                self.U_S,self.U_B,self.negotiations = self.negotiate(i,j)
                                if self.negotiations[i][j] == 1:   #协商成功，i j 重新加入匹配
                                    print("匹配轮：",r)
                                    break    
            r += 1
            #未匹配买家的更新信息
            for j in Nb:
                if j not in matched_b_indices:
                    a = self.buyers[j].lambda_j
                    self.buyers[j].lambda_j = np.round(random.uniform(a, 1),2)
                else:
                    break
            for i in Ns:
                if i not in matched_s_indices:
                    if self.sellers[i].p_ < self.sellers[i].p and self.sellers[i].p > 0:
                        b = self.sellers[i].pi
                        self.sellers[i].pi = random.randint(0, 10)
                        if self.sellers[i].pi == b:
                            self.sellers[i].pi = random.randint(0, 10)
            Match = 0
            self.matches = [[0] * len(self.buyers) for _ in range(len(self.sellers))]  
            self.negotiations = [[0] * len(self.buyers) for _ in range(len(self.sellers))]
            self.A_S = [[0] * len(self.buyers) for _ in range(len(self.sellers))]  # 初始化卖家意向矩阵   
            self.A_B = [[0] * len(self.sellers) for _ in range(len(self.buyers))] 
        return self.matches,self.U_S,self.U_B,self.negotiations   


    def negotiate(self, i, j):
        # 初始化参数
        k = 1
        self.P_S[i][j] = self.buyers[j].pj
        self.lambda_S[i][j] = self.sellers[i].lambda_i       
        self.P_B[j][i] = self.buyers[j].pj
        self.lambda_B[j][i] = self.buyers[j].lambda_j 
        print("初始")
        print(self.P_S[i][j])
        print(self.lambda_S[i][j])
        print(self.P_B[j][i])
        print(self.lambda_B[j][i])
        #上一轮的值
        a_SP = self.P_S[i][j]
        b_Sl = self.lambda_S[i][j] 
        c_BP = self.P_B[j][i]
        d_Bl = self.lambda_B[j][i]

        while k <= self.K:
            # 卖家协商逻辑
            lambda_r_S = self.alpha_S[i] * c_BP + self.beta_S[i] * (1 + self.g_S[i]) - self.tau[i][j]
            if abs(lambda_r_S - d_Bl) < self.epsilon:
                self.P_S[i][j] = c_BP
                self.lambda_S[i][j] = self.alpha_S[i] * self.P_S[i][j] + self.beta_S[i] * (1 + self.g_S[i]) - self.tau[i][j]
            else:
                if abs(a_SP - c_BP) < self.epsilon:
                    if d_Bl >= b_Sl:
                        self.lambda_S[i][j] = (b_Sl + d_Bl) / 2
                    else:
                        self.lambda_S[i][j] = max(lambda_r_S, b_Sl - self.mu_lambda)
                    self.P_S[i][j] = c_BP
                else:
                    self.g_S[i] = max(0, self.g_S[i] - self.mu_g)
                    self.P_S[i][j] = max(self.buyers[j].pj, a_SP - self.mu_p * (a_SP - c_BP))
                    self.lambda_S[i][j] = self.alpha_S[i] * self.P_S[i][j] + self.beta_S[i] * (1 + self.g_S[i]) - self.tau[i][j]

            # 买家协商逻辑
            lambda_r_B = -self.alpha_B[j] * a_SP + self.beta_B[j] * (1 - self.g_B[j]) - self.tau[i][j]
            if abs(lambda_r_B - b_Sl) < self.epsilon:
                self.P_B[j][i] = min(self.buyers[j].pj, a_SP)
                self.lambda_B[j][i] = -self.alpha_B[j] * self.P_B[j][i] + self.beta_B[j] * (1 - self.g_B[j]) - self.tau[i][j]
            else:
                if abs(c_BP - a_SP) < self.epsilon:
                    if b_Sl <= d_Bl:
                        self.lambda_B[j][i] = (b_Sl + d_Bl) / 2
                    else:
                        self.lambda_B[j][i] = min(lambda_r_B, d_Bl + self.mu_lambda)
                    self.P_B[j][i] = a_SP
                else:
                    self.g_B[j] = max(0, self.g_B[j] - self.mu_g)
                    self.P_B[j][i] = min(self.buyers[j].pj, c_BP + self.mu_p * (c_BP - a_SP))
                    self.lambda_B[j][i] = -self.alpha_B[j] * self.P_B[j][i] + self.beta_B[j] * (1 - self.g_B[j]) - self.tau[i][j]

            # 检查循环条件
            if (abs(self.P_B[j][i] - self.P_S[i][j]) <= self.epsilon and abs(self.lambda_B[j][i] - self.lambda_S[i][j]) <= self.epsilon) :
                    self.negotiations[i][j] = 1
                    self.U_S[i] = self.U_S[i] + self.P_S[i][j] * self.lambda_S[i][j] - 1/2 * self.alpha_S[i] * (self.P_S[i][j] ** 2) - self.beta_S[i] * self.P_S[i][j]
                    self.U_B[j] = self.U_B[j] + self.P_B[j][i] * self.lambda_B[j][i] 
                    self.sellers[i].p -= self.P_S[i][j]
                    self.buyers[j].p -= self.P_B[j][i]
                    print("协商成功")
                    print(self.P_S[i][j])
                    print(self.lambda_S[i][j])
                    print(self.P_B[j][i])
                    print(self.lambda_B[j][i])
                    break

            # 更新这一轮的变化变量
            a_SP = self.P_S[i][j]
            b_Sl = self.lambda_S[i][j]
            c_BP = self.P_B[j][i]
            d_Bl = self.lambda_B[j][i]
            print("协商后")
            print(self.P_S[i][j])
            print(self.lambda_S[i][j])
            print(self.P_B[j][i])
            print(self.lambda_B[j][i])
            # 更新轮次
            k += 1

        return self.U_S,self.U_B,self.negotiations




