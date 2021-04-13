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
        
    def step(self,action):
        r,c = self.current_state

        if action == 0:
            r -=1
        if action == 1:
            c -=1
        if action == 2:
            r +=1
        if action == 3:
            c +=1

        reward = self.step_reward
        done = False
        
        if 0 <= r <= self.rows - 1 and 0 <= c <= self.cols - 1:
            if (r,c) not in self.walls:
                if (r,c) in self.terminal_states:
                    reward = self.terminal_states[(r,c)]

                    done = True
                self.current_state = (r,c)
        return self.current_state,reward,done
    
    def all_states(self):
        self.states = []
        for r in range(self.rows):
            for c in range(self.cols):
                self.states.append((r,c))
                
    def reset(self):
        self.current_state = self.initial_state
        return self.initial_state


            

        
