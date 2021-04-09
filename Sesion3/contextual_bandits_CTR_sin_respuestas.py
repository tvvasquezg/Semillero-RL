#Este código simula el problema de escoger el mejor diseño de un anuncio
#publicitario tal que el usuario haga click que lo lleve a la página
#que ofrece el producto/servicio. El problema recide en el hecho que no
#se sabe cuál de todos los diseños hará más probable que el usuario de click
#(se asume que no se conoce cual es el valor real de cada acción del Agente).
#Además, hay 3 tipos de usuarios que entran a la página independientemente de
#quien haya entrado antes.

#Se debe resolver este problema inicializando los valores reales de cada acción.
#Además de crear la función de reward.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
#K representa el número de diseños distintos de un banner 
K = 10

n_states = 3
#Cada q o número del array representa la probabilidad de
#un usuario cualquiera de hacer click en el anuncio correspondiente
#COMPLETAR
qs = #???


#Función que permite al Agente tomar una acción. Usa epsilon-greedy
#para balancear entre la exploración y explotación
#Input: epsilon
#Output: acción avara con 1 - epsilon de probabilidad y acción al azar
#con epsilon de probabilidad

def choose_action(state,epsilon=0.1):
    p = np.random.rand()
    if p < epsilon:
        return np.random.choice(K)
    else:
        return np.argmax(Qs[state])

#COMPLETAR
def get_reward(state,action):
    pass
    
def get_state():
    return np.random.choice(n_states)
    
timesteps = 10_000

Qs = np.zeros((n_states,K))
epsilon = 0.01
alpha = 0.01
rewards = []

for t in range(timesteps):
    state = get_state()
    action = choose_action(state,epsilon)
    reward = get_reward(state,action)
    
    Qs[state,action] += alpha*(reward - Qs[state,action])
    rewards.append(reward)

print('Rewards ganados:',np.sum(rewards))
plt.plot(np.cumsum(rewards)/(np.arange(len(rewards))+1))
plt.show()


    




