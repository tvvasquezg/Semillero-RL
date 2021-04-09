#Este código simula el problema de escoger el mejor diseño de un anuncio
#publicitario tal que el usuario haga click que lo lleve a la página
#que ofrece el producto/servicio. El problema recide en el hecho que no
#se sabe cuál de todos los diseños hará más probable que el usuario de click
#(se asume que no se conoce cual es el valor real de cada acción del Agente).

#Se debe resolver este problema creando un Agente que escoja siempre el mejor
#de los diseños. Para esto se debe completar la función choose_action.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
#K representa el número de diseños distintos de un banner 
K = 10

#Cada q o número del array representa la probabilidad de
#un usuario cualquiera de hacer click en el anuncio correspondiente
qs = np.round(np.random.rand(K)*0.03,3)


#Función que permite al Agente tomar una acción. Usa epsilon-greedy
#para balancear entre la exploración y explotación
#Input: epsilon
#Output: acción avara con 1 - epsilon de probabilidad y acción al azar
#con epsilon de probabilidad.
#SUGERENCIA: Comenzar con el método epsilon-greedy y después implementar
#otros

#COMPLETAR
def choose_action(epsilon=0.1):
    pass


def get_reward(action):
    p = np.random.rand()
    return 1 if p < qs[action] else 0
    
    
timesteps = 10_000

Qs = np.zeros((K))
epsilon = 0.01
alpha = 0.01
rewards = []

for t in range(timesteps):
    action = choose_action(epsilon)
    reward = get_reward(action)
    
    Qs[action] += alpha*(reward - Qs[action])
    rewards.append(reward)

print('Rewards ganados:',np.sum(rewards))

plt.plot(np.cumsum(rewards)/(np.arange(len(rewards))+1))
plt.show()


    




