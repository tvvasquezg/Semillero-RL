from visualizer import *

#Sirve para comparar más fácilmente cada agente.
np.random.seed(1)

K = 3

qs = np.random.randint(-5,5,size=K)
Qs = np.zeros(K)
Ns = np.zeros(K)


#Función get_reward:
#input:acción.
#Output: Un reward muestreado de la distribución asociada a la acción ingresada.
#Esta distribucion tiene una media = qs[action] (el valor real de la acción tomada)
#y desviación estandar escogida por el programador.

def get_reward(action):
    return np.random.normal(qs[action],1)

#Input:Epsilon (la probabilidad de tomar una acción al azar). 
#Output:Acción. Con probabilidad epsilon retorna una acción al azar.
#Con probabilidad 1 - epsilon retorna una acción avara (greedy action)
def choose_action(epsilon=0.1):
    p = np.random.rand()

    if p < epsilon:
        return np.random.choice(K)
    else:
        return np.argmax(Qs)

epsilon = 0.1
timesteps = 1_000
v = Visualizer(epsilon,timesteps,qs,Qs)
rewards = np.zeros(timesteps)

for t in range(timesteps):
    action = choose_action(epsilon)
    reward = get_reward(action)
    rewards[t] = reward
    Ns[action] +=1
    Qs[action] += (1/Ns[action])*(reward - Qs[action])
    v.render(action,reward,epsilon,t)
#rewards obtained in experiment

#rewards = #render(alpha,epsilon,timesteps,choose_action,get_reward)

graph([rewards],[epsilon])




