import numpy as np
import matplotlib.pyplot as plt

def run_experiment(alpha,epsilon,timesteps,timestep_of_change,n_actions):
    qs = np.random.normal(0,1,size=n_actions)*10
    qss = [qs]
    qss.append(np.random.permutation(qs))
    Qs = np.zeros(n_actions)

    def get_reward(qs,action):
        return np.random.normal(qs[action])

    def choose_action(epsilon=0.001):
        p = np.random.rand()

        if p < epsilon:
            return np.random.choice(n_actions)
        else:
            return np.argmax(Qs)



    qs = qss[0]
    change = True
    rewards = np.zeros(timesteps)
    for t in range(timesteps):
        if t >= timestep_of_change and change:
            change = False
            qs = qss[1]
        action = choose_action(epsilon)
        reward = get_reward(qs,action)
        #print(reward)
        rewards[t] = reward
        Qs[action] += alpha*(reward - Qs[action])

    avg_rewards = np.cumsum(rewards)/(np.arange(timesteps)+1)
    mini,maxi = min(avg_rewards),max(avg_rewards)
    title = 'Agent updating with alpha'+'\n'+str(np.round(qss[0],2))+'\n'+str(np.round(qss[1],2))
    plt.title(title)
    plt.plot(avg_rewards)
    plt.vlines(timestep_of_change,mini,maxi,colors='r',linestyles='dashed')
    plt.ylabel('Average reward')
    plt.xlabel('Timesteps')
    plt.show()
