import numpy as np
import matplotlib.pyplot as plt
from record import Record
from visualizer import visualize

r = Record(10)

n_states = 2
K = 5

qs = np.array([[1,0,0,0,0],[0,1,0,0,0]])

Qs = np.zeros((n_states,K))
Ns = np.zeros((n_states,K))

def get_reward(state,action):
    return np.random.normal(qs[state,action])

def choose_action(state,epsilon=0.1):
    p = np.random.rand()

    if p < epsilon:
        action = np.random.choice(K)
        #print('action',action)
        return action
    else:
        max_idxs = np.where(Qs[state] == np.max(Qs[state]))[0]
        if len(max_idxs)>1:
            max_idx = np.random.choice(max_idxs)
        else:
            return np.argmax(Qs[state])
        action = max_idx
        
        return action

def choose_random_state(previous_state):
    state = np.random.choice(n_states)
    while state == previous_state:
        state = np.random.choice(n_states)
    return state


timesteps = 10_000
rewards = np.zeros(timesteps)
state = 0
for t in range(100):
    state = choose_random_state(state)
    action = choose_action(state)
    #print(state,action)
    r.record_baseline(state,action)

#print('r.base_line[:][1]',r.base_line[:,1])
visualize(r.base_line[:,0],r.base_line[:,1],10,(255,0,0))

for t in range(timesteps):
    
    state = choose_random_state(state)
    action = choose_action(state)
    if t>300:
        r.record_while_learning(state,action)
    reward = get_reward(state,action)
    rewards[t] = reward
    Ns[state,action] +=1
   # print('Qs[state,action]',Qs[state,action])
    Qs[state,action] = Qs[state,action] + (1/Ns[state,action])*(reward - Qs[state,action]) 
visualize(r.learning[:,0],r.learning[:,1],10,(0,0,0))

for t in range(100):
    state = choose_random_state(state)
    action = choose_action(state,epsilon=0)
    r.record_in_test(state,action)

visualize(r.test[:,0],r.test[:,1],10,(0,255,0))
plt.plot(np.cumsum(rewards)/(np.arange(timesteps)+1))
plt.show()



    





