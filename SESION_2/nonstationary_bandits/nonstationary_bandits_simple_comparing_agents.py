#Número variable de cambios de valor de acciones
#Tabla (o graficos de desempeño según distintos hiperparametros
# o cambios en el ambiente)

import numpy as np
import matplotlib.pyplot as plt
from comparing_agents import run_experiment

np.random.seed(5) #para permitir replicación del experimento

K = 5 #número de acciones posibles

epsilon = 0.1
alpha = 0.01
timesteps = 200_000

timestep_of_change = 35000




run_experiment(alpha,epsilon,timesteps,timestep_of_change,n_actions=K)
