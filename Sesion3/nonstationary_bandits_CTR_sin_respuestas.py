#Este código simula el problema de escoger el mejor diseño de un anuncio
#publicitario tal que el usuario haga click que lo lleve a la página
#que ofrece el producto/servicio. El problema recide en el hecho que no
#se sabe cuál de todos los diseños hará más probable que el usuario de click
#(se asume que no se conoce cual es el valor real de cada acción del Agente).

#Todo está listo excepto implementar el experimento. El loop principal que iterará
#un número de veces determinado por la variable timesteps. Este loop tendra
#la interacción entre el Agente y el Ambiente. Entiendase por interacción
#a las acciones que toma el agente y los rewards recibidos producto de estas.
#También el aprendizaje del Agente está dentro de este loop. Finalmente, que métrica
#usarás para evaluar el desempeño del agente

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(50)
#K representa el número de diseños distintos de un banner 
K = 10

#Cada q o número del array representa la probabilidad de
#un usuario cualquiera de hacer click en el anuncio correspondiente
qs = np.round(np.random.rand(K)*0.03,3)


#Función que permite al Agente tomar una acción. Usa epsilon-greedy
#para balancear entre la exploración y explotación
#Input: epsilon
#Output: acción avara con 1 - epsilon de probabilidad y acción al azar
#con epsilon de probabilidad

#COMPLETAR
def choose_action(epsilon=0.1):
    p = np.random.rand()
    if p < epsilon:
        return np.random.choice(K)
    else:
        return np.argmax(Qs)


def get_reward(action):
    p = np.random.rand()
    return 1 if p < qs[action] else 0
    
    
timesteps = 10_000

Qs = np.zeros((K))
epsilon = 0.01
alpha = 0.001
rewards = []

changes_in_qs = [1000,4200]


#Realiza el experimento!
for t in range(timesteps):
    #????


    




