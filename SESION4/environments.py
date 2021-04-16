import numpy as np
from agents import MCAgent



class Env:
    def __init__(self,rows,cols,walls,terminal_states,step_reward=1):
        self.rows = rows
        self.cols = cols
        self.walls = walls
        self.terminal_states = terminal_states
        self.initial_state = (rows-1,0)
        self.current_state = self.initial_state
        self.all_states()
        self.step_reward = step_reward

    def get_reward(self):
        return self.step_reward
    
    def transition(self,action):
        r,c = self.current_state

        if action == 0:
            r -=1
        if action == 1:
            c -=1
        if action == 2:
            r +=1
        if action == 3:
            c +=1
        return r,c
        
    def step(self,action):
        r,c = self.transition(action)#r,c = self.current_state

##        if action == 0:
##            r -=1
##        if action == 1:
##            c -=1
##        if action == 2:
##            r +=1
##        if action == 3:
##            c +=1

        reward = self.get_reward()
        done = False
        
        if 0 <= r <= self.rows - 1 and 0 <= c <= self.cols - 1:
            if (r,c) not in self.walls:
                if (r,c) in self.terminal_states:
                    #if (r,c) == self.terminal_states[0]:
                    reward = self.terminal_states[(r,c)]
                    #else:
                     #   reward = -1
                    done = True
                self.current_state = (r,c)
        return self.current_state,reward,done

                
    def reset(self):
        self.current_state = self.initial_state
        return self.initial_state
    
    def all_states(self):
        self.states = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r,c) not in self.walls:
                    self.states.append((r,c))
        
                    


class EnvRStoch(Env):
    def __init__(self,rows,cols,walls,terminal_states,reward_dist=[[2/3,-0.02],[1/3,-0.01],[0/3,0.0]]):
        Env.__init__(self,rows,cols,walls,terminal_states)
        self.reward_dist = np.array(reward_dist)
    def get_reward(self):
        return np.random.choice(self.reward_dist[:,1],p=self.reward_dist[:,0])


class EnvTStoch(EnvRStoch):
    def __init__(self,rows,cols,walls,terminal_states,reward_dist=[[2/3,-0.02],[1/3,-0.01],[0/3,0.0]],action_transition=0.7):
        EnvRStoch.__init__(self,rows,cols,walls,terminal_states,reward_dist)
        self.action_transition_p = action_transition
        self.action_space = [a for a in range(4)]
        
    def transition(self,action):
        r,c = self.current_state
        p = np.random.rand()

        
        if action == 0:
            if p < self.action_transition_p:
                r -=1
            else:
                
                av_action_space = list(set(self.action_space) - set([action]))
                a = np.random.choice(av_action_space)
                
                if a == 1:
                    c -= 1
                elif a == 2:
                    r += 1
                elif a == 3:
                    c += 1
                    
        if action == 1:
            if p < self.action_transition_p:
                c -=1
            else:
                av_action_space = list(set(self.action_space) - set([action]))
                a = np.random.choice(av_action_space)
                
                if a == 0:
                    r -= 1
                elif a == 2:
                    r += 1
                elif a == 3:
                    c += 1
        if action == 2:
            if p < self.action_transition_p:
                r +=1
            else:
                av_action_space = list(set(self.action_space) - set([action]))
                a = np.random.choice(av_action_space)
                
                if a == 0:
                    r -= 1
                elif a == 1:
                    c -= 1
                elif a == 3:
                    c += 1
                    
        if action == 3:
            if p < self.action_transition_p:
                c +=1
            else:
                av_action_space = list(set(self.action_space) - set([action]))
                a = np.random.choice(av_action_space)
                
                if a == 0:
                    r -= 1
                elif a == 1:
                    c -= 1
                elif a == 2:
                    r += 1
        return r,c
            
e = EnvTStoch(3,4,[(1,1)],{(0,3):1,(1,3):-1})


if __name__ == '__main__':
    e = EnvRStoch(3,4,[(1,1)],{(0,3):1,(1,3):-1})
    for i in range(10):
        print(e.get_reward())        
