#AGENTE MC 10:04

import numpy as np
from constants import *


class MCAgent:
    def __init__(self,env,action_space,epsilon=0.1):
        self.env = env
        self.action_space = action_space
        self.n_actions = len(action_space)
        self.epsilon = epsilon
        self.states = self.env.states
        self.Qs = self.init_Qs()
        
        
    def init_Qs(self):
        Qs = {}
        for s in self.states:
            Qs[s] = {}
            for a in range(self.n_actions):
                Qs[s][a] = 0
        return  Qs
    def choose_action(self,state):
        p = np.random.rand()
        if p < self.epsilon:
            return np.random.choice(self.action_space)
        else:
            best_action = None
            best_value = float('-inf')
            for a in self.action_space:
                if self.Qs[state][a]>best_value:
                    best_value = self.Qs[state][a]
                    best_action = a
            
            return a  
                    

    def get_return(self,states_actions_rewards):
        G = 0
        sars = states_actions_rewards
        states_actions_returns = [(sars[-1][0],sars[-1][1],G)]
        for s,a,r in reversed(sars[:-1]):
            G = r + GAMMA*G
            states_actions_returns.append((s,a,G))
        return states_actions_returns

    def update(self,states_actions_rewards):
        states_actions_returns = self.get_return(states_actions_rewards)
        sars = states_actions_returns
        for s,a,G in sars:
            self.Qs[s][a] = self.Qs[s][a] + ALPHA*(G - self.Qs[s][a])
            #self.Qs[s][a][1] = np.mean(self.Qs[s][a][0])
        
class QAgent:
    def __init__(self,env,alpha=1,epsilon=1,gamma=0,):
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
            
                                
    

if __name__ == '__main__':
            
    sars = [(0,'u',1),(1,'l',-2),(2,'l',5),(3,None,0)]
    gamma = 0.5
    print(get_return(sars))


    



            
