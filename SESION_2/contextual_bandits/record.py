import numpy as np

class Record:
    def __init__(self,n_timesteps):
        self.n_timesteps = n_timesteps
        self.base_line = np.zeros((n_timesteps,2))
        self.idx_baseline = 0
        self.learning = np.zeros((n_timesteps,2))
        self.idx_learning = 0
        self.test = np.zeros((n_timesteps,2))
        self.idx_test = 0
    def record_baseline(self,state,action):
        if self.idx_baseline<self.n_timesteps:
            self.base_line[self.idx_baseline] = [state,action]
            self.idx_baseline +=1
    def record_while_learning(self,state,action):
        if self.idx_learning<self.n_timesteps:
            self.learning[self.idx_learning] = [state,action]
            self.idx_learning +=1
    def record_in_test(self,state,action):
        if self.idx_test<self.n_timesteps:
            self.test[self.idx_test] = [state,action]
            self.idx_test +=1
