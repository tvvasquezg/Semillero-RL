import numpy as np
import matplotlib.pyplot as plt

def run_experiment(alpha,epsilon,timesteps,timestep_of_change,n_actions):

    qs = np.random.normal(0,1,size=n_actions)*10
    qss = [qs]
    qss.append(np.random.permutation(qs))
    Qs = np.zeros(n_actions)
    Qs_alpha = np.zeros(n_actions)
    Ns = np.zeros(n_actions)

    def get_reward(qs,action):
        return np.random.normal(qs[action])

    def choose_action(Qs,epsilon=0.001):
        p = np.random.rand()

        if p < epsilon:
            return np.random.choice(n_actions)
        else:
            return np.argmax(Qs)



    qs = qss[0]
    change = True
    rewards = np.zeros(timesteps)
    rewards_alpha = np.zeros(timesteps)
    for t in range(timesteps):
        if t >= timestep_of_change and change:
            change = False
            qs = qss[1]
        action = choose_action(Qs,epsilon)
        action_alpha = choose_action(Qs_alpha,epsilon)
        reward = get_reward(qs,action)
        reward_alpha = get_reward(qs,action_alpha)
        
        #print(reward)
        rewards[t] = reward
        rewards_alpha[t] = reward_alpha
        
        Ns[action] +=1
        Qs[action] += (1/Ns[action])*(reward - Qs[action])
        Qs_alpha[action_alpha] += alpha*(reward_alpha - Qs_alpha[action_alpha])

    avg_rewards = np.cumsum(rewards)/(np.arange(timesteps)+1)
    avg_rewards_alpha = np.cumsum(rewards_alpha)/(np.arange(timesteps)+1)
    mini,maxi = min(avg_rewards),max(avg_rewards)
    title = 'Comparing Agent updating with 1/n(a) and Agent updating with alpha'+'\n'+str(np.round(qss[0],2))+'\n'+str(np.round(qss[1],2))
    plt.title(title)
    plt.plot(avg_rewards,label='1/n')
    plt.plot(avg_rewards_alpha,label='alpha%.3f'%(alpha))
    plt.vlines(timestep_of_change,mini,maxi,colors='r',linestyles='dashed')
    plt.ylabel('Average reward')
    plt.xlabel('Timesteps')
    plt.legend()
    plt.show()
