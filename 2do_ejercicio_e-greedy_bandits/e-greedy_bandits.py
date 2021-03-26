from visualizer import *

#SUGERENCIAS:
#-Empezar modificando epsilon y ver el comportamiento del
# agente con diferentes valores
#-Modificar qs (e.g. cambiar la distribución de una normal a una uniforme etc)
#-Modificar timesteps (número de intentos que tiene el agente)
#-Modificar el número de acciones. ADVERTENCIA: La visualización no funciona
# con un K != 3 por lo que para modificar el número de acciones posibles se
# deberá comentar 2 lineas de código responsables de la visualización del agente.


#np.random.seed(1)

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
    #???

#Input:Epsilon (la probabilidad de tomar una acción al azar). 
#Output:Acción. Con probabilidad epsilon retorna una acción al azar.
#Con probabilidad 1 - epsilon retorna una acción avara (greedy action)

def choose_action(epsilon=0.1):
    #???

epsilon = 0.1
timesteps = 1_000
v = Visualizer(epsilon,timesteps,qs,Qs)
rewards = np.zeros(timesteps)

for t in range(timesteps):
    action = choose_action(epsilon)
    reward = get_reward(action)
    rewards[t] = reward
    Qs[action] += (1/Ns[action])*(reward - Qs[action])
    v.render(action,reward,epsilon,t)
#rewards obtained in experiment

#rewards = #render(alpha,epsilon,timesteps,choose_action,get_reward)

graph([rewards],[epsilon])




