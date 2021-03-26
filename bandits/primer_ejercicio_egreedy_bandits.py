from visualizer import *
from rewards_actions import get_reward,choose_action
#Sirve para comparar más fácilmente cada agente.
np.random.seed(1)

K = 3 #MODIFICALO!!

qs = np.random.randint(-5,5,size=K) #MODIFICALO!!
Qs = np.zeros(K) #MODIFICALO!!
Ns = np.zeros(K)




epsilon = 0.01 #MODIFICALO!!
timesteps = 1_000 #MODIFICALO!!

v = Visualizer(epsilon,timesteps,qs,Qs)

rewards = np.zeros(timesteps)

for t in range(timesteps):
    action = choose_action(Qs,epsilon)
    reward = get_reward(qs,action)
    rewards[t] = reward
    Ns[action] +=1
    Qs[action] += (1/Ns[action])*(reward - Qs[action])
    v.render(action,reward,epsilon,t)
#rewards obtained in experiment

#rewards = #render(alpha,epsilon,timesteps,choose_action,get_reward)

graph([rewards],[epsilon])




