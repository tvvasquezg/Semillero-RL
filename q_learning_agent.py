import numpy as np
import matplotlib.pyplot as plt

ALPHA = 0.5
BETA = 0.5 
ETA = 0.9
LAMBDA = 5
N_TRIALS = 100
N_BINS = 10
N_EPISODES = 20

#array de valores para discretizar el espacio o conjunto de states continuo 
discretization = np.linspace(0, LAMBDA, N_BINS)
v = 0

#Agente de RL. Usa q-learning
class Agent:
    def __init__(self, alpha=0.1, epsilon=0.01, gamma=0.9):
        #Asume un mdp con 10 estados (discretización del espacio en 10 bins)
        self.q_values = np.zeros((N_BINS, 2))

        self.alpha = alpha 
        self.epsilon = epsilon 
        self.gamma = gamma 

    #Selecciona acción según epsilon y tabla de valores q
    def action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice([0, 1])
        else:
            return np.argmax(self.q_values[state])
    
    #algoritmo de q learning para actualizar valores de estado y accion (Q(s,a))
    def learn(self, state, action, next_state, reward, done):
        if done:
            target_value = reward 
        else:
            max_next_value = np.max(self.q_values[next_state])
            target_value = reward + self.gamma*max_next_value
        
        self.q_values[state, action] += self.alpha*(target_value - self.q_values[state, action])

#Función de refuerzo que incentiva al agente de RL 
#para enseñar a predecir al modelo conductual a 
#predecir lo más rápido posible
def reward_function(lambd, current_state):
    #N_BINS - 1 es el indice correspondiente a la máxima predicción del modelo conductual
    #i.e., el terminal state o meta del agente
    if current_state == N_BINS - 1:
        return 1

    return -0.01

#retorna el state en forma de número entero desde un valor continuo
def get_state(new_v):
    return np.digitize(new_v, discretization)



#función que entrena al agente de RL 
#para que a su vez entrene al modelo conductual
#según función de refuerzo
def agent_training(agent):
    
    vs = []
    rewards = []
    n_episode_steps = []
    for episode in range(N_EPISODES):
        episode_reward = 0.0
        v = 0.0
        print('episode', episode)
        for t in range(N_TRIALS):
            old_v = get_state(v)
            
            agent_action = agent.action(old_v)
            #print('step', t, 'state', old_v, 'action', agent_action)
            dv = ALPHA*BETA*(LAMBDA - v)
            if agent_action:
                v += dv
            else:
                    #Invento mio para producir alguna curva algo similar a lo esperado en la extinción
                    #Hay que averiguar como el modelo de Rescorla Wagner modela el proceso de extinción
                    #(si es que lo hace)
                v *= ETA

            new_v = get_state(v)
            reward = reward_function(LAMBDA, new_v)
            episode_reward += reward

            done = 1 if new_v == N_BINS - 1 else 0
            agent.learn(old_v, agent_action, new_v, reward, done)
            vs.append(v)
            if done or t == N_TRIALS - 1:
                print('n steps per episode', t)
                n_episode_steps.append(t + 1)
                break 
    
        rewards.append(episode_reward)

        
    
    return vs, rewards, n_episode_steps

agent = Agent()
vs,rewards, n_episode_steps = agent_training(agent)
n_episode_steps = np.cumsum(n_episode_steps)


plt.scatter([x for x in range(len(vs))], vs, s=3)
plt.title('Prediction Value of Behavioral Model per Episode')
for nes in n_episode_steps:
    print('nes', nes)
    plt.axvline(x=nes, linestyle='--', c='r')

plt.show()        
plt.scatter([x for x in range(len(rewards))], rewards, c='g')        
plt.plot([x for x in range(len(rewards))], rewards, c='g')        
plt.xticks([x for x in range(len(rewards))], [x for x in range(len(rewards))])
plt.title('Amount of Reward Gained by RL Agent per Episode')
plt.show()

