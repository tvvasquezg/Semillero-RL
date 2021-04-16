import numpy as np


GAMMA = 1

#EJERCICIO 1

#Lista con tuplas (Estado,Refuerzo(t))
seq_states_rewards = [(0,0),(1,3),(2,-1),(3,5),(4,10)]
#Lista con tuplas (Estado,Refuerzo(t+1)
seq_states_rewards = [(0,3),(1,-1),(2,5),(3,10),(4,0)] 

#HAGA UNA FUNCIÓN QUE CALCULE EL RETORNO PARA CADA UNO DE LOS ESTADOS
def calculate_return(sequence_states_rewards):
    G = 0
    ssr = sequence_states_rewards
    seq_states_returns = [(ssr[-1][0],G)]
    

    for s,r in reversed(ssr[:-1]):
        G = r + GAMMA*G
        seq_states_returns.append((s,G))

    seq_states_returns.reverse()
    return seq_states_returns


print(calculate_return(seq_states_rewards))


#RESPUESTA CORRECTA
#GAMMA = 1
#s,G
#0,17
#1,14
#2,15
#3,10
#4,0

        
