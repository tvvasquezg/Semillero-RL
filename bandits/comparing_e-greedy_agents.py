from visualizer import *


#np.random.seed(2)

K = 3

qs = np.random.randn(3)*10#np.random.randint(-5,5,size=K)
qs = np.round(qs,1)
Qs = np.zeros(K)
Ns = np.zeros(K)

def get_reward(action):
    return np.random.normal(qs[action],0.5)

def choose_action(epsilon=0.1):
    p = np.random.rand()

    if p < epsilon:
        return np.random.choice(K)
    else:
        return np.argmax(Qs)


timesteps = 1_000


list_of_rewards = []

print('qs',qs)
for i in range(3):
    
    rewards = np.zeros(timesteps)
    epsilons = [0.0,0.1,0.01]
    epsilon = epsilons[i]
    Qs = np.zeros(K)
    
    v = Visualizer(epsilon,timesteps,qs,Qs)
    for t in range(timesteps):
        action = choose_action(epsilon)
        reward = get_reward(action)
        rewards[t] = reward
        Ns[action] +=1
        Qs[action] += (1/Ns[action])*(reward - Qs[action])
        v.render(action,reward,epsilons[i],t)
    print('Epsilon: ',epsilons[i],' - ','total rewards obtained: ',np.sum(rewards))
    list_of_rewards.append(rewards)
    
#rewards obtained in experiment

#rewards = #render(alpha,epsilon,timesteps,choose_action,get_reward)

print(list_of_rewards[0][:20])
print(list_of_rewards[1][:20])
print(list_of_rewards[2][:20])

graph(list_of_rewards,epsilons)



