class Seller:  
    def __init__(self, pi, lambda_i, p_, p):  
        self.pi = pi  
        self.lambda_i = lambda_i 
        self.p_ = p_
        self.p = p

class Buyer:  
    def __init__(self, pj, lambda_j, p_, p):  
        self.pj = pj                         #电量，一般等于p
        self.lambda_j = lambda_j #价格，心理预期的单位电价
        self.p_ = p_             #最低电量需求
        self.p = p                  #最高电量需求