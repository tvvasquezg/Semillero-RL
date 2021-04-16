#FALTA AUTOMATIZAR LA ASIGNACION DE NOMBRES DE COLUMNAS CON ESTADOS
import numpy as np
from agents import QAgent
from environments import *
from visualizer import visualize
from calculate_G import calculate_return
import pandas as pd

def uniform_random_policy(state):
    return np.random.choice(4)




optimal_policy = {
        (1,0):0,
        (0,0):3,
        (0,1):3,
        (0,2):2
    }

    

env = EnvTStoch(2,3,[(1,1)],{(1,2):1},reward_dist=[[1,-0.05]],action_transition=1)
#env = EnvTStoch(2,3,[(1,1)],{(1,2):1},reward_dist=[[1,-0.05]],action_transition=0.5)
#env = EnvTStoch(2,3,[(1,1)],{(1,2):1},reward_dist=[[0.3,-1],[0.5,-0.7],[0.2,-0.2]],action_transition=0.5)
episodes = 20
capture_every = 10

#MISMA POLÍTICA
Gss = {}

for e in range(episodes):
    s = env.reset()
    done = False
    first = True
    path = [s]
    state_action_rewards = []
    states_rewards = []
    
    while not done:
        
            
        a = optimal_policy[s]#uniform_random_policy(s)#agent.choose_action(s)
        next_s,reward,done = env.step(a)
        state_action_rewards.append((s,a,reward))
        states_rewards.append((s,reward))
        s = next_s
        if done:
            states_rewards.append((s,0))
        if e%capture_every == 0:
            path.append(s)

    ss_Gs = calculate_return(states_rewards)

    for s in ss_Gs:
        if s not in Gss:
            Gss[s] = []
        Gss[s].append(ss_Gs[s])
    n_states=  len(ss_Gs)
    if e%capture_every == 0:
        #pass
        visualize(env,None,path,value_function=False)
ar_Gs = np.zeros(episodes)


for Gs in Gss.values():
    #for s in ss_Gs:
        ar_Gs = np.vstack((ar_Gs,Gs))

ar_Gs = np.round(ar_Gs[1:,:].T,3)

ar_Gs[:,[c for c in reversed(range(ar_Gs.shape[1]))]] = ar_Gs[:,[c for c in range(ar_Gs.shape[1])]] 

df = pd.DataFrame(data=ar_Gs,    # values
             columns=[(1,0),(0,0),(0,1),(0,2),(1,2)])
              #index=data[1:,0],    # 1st column as index
              
print(df)
print(np.mean(ar_Gs,axis=0))

