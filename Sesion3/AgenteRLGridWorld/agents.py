import numpy as np
        
class QAgent:
    def __init__(self,env,alpha=1,epsilon=1,gamma=0):
        self.env = env
        self.states = self.env.states
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.action_space = [a for a in range(4)]
        self.n_actions = len(self.action_space)
        self.Qs = np.zeros((self.env.rows,self.env.cols,self.n_actions))

    def choose_action(self,state):
        p = np.random.rand()
        if p < self.epsilon:
            return np.random.choice(self.action_space)
        else:
            return np.argmax(self.Qs[state])
    def update(self,state,action,next_s,reward,done):
        if done:
            target = reward
        else:
            target = reward + self.gamma*np.max(self.Qs[next_s])
        self.Qs[state[0],state[1],action] += self.alpha*(target - self.Qs[state[0],state[1],action])
            
                               
