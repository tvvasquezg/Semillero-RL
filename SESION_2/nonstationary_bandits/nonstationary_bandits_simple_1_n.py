#Número variable de cambios de valor de acciones
#Tabla (o graficos de desempeño según distintos hiperparametros
# o cambios en el ambiente)

import numpy as np
import matplotlib.pyplot as plt
from simple_1_n import run_experiment

np.random.seed(2)

K = 5 #número de acciones posibles

epsilon = 0.1
timesteps = 10_000

timestep_of_change = 500




run_experiment(epsilon,timesteps,timestep_of_change,n_actions=K)          

