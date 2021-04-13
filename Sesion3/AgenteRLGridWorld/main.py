import numpy as np
from agents import QAgent
from environments import Env
from visualizer import visualize

#Modifiquen uno de los parámetros del ambiente para que el agente pueda llegar al cuadro verde!
env = Env(5,6,walls = [(1,1)],terminal_states = {(0,3):1,(1,3):-1},step_reward = 1)

#Modifiquen los parámetros del agente para que pueda llegar al cuadro verde!
#...pero también exploren lo que quieran...experimenten y registren los resultados!
agent = QAgent(env,alpha = 1,epsilon = 1,gamma = 0)


episodes = 10_000
capture_every = 1

for e in range(episodes):
    s = env.reset()
    done = False
    first = True
    path = [s]
    while not done:
        
            
        a = agent.choose_action(s)
        next_s,reward,done = env.step(a)
        agent.update(s,a,next_s,reward,done)
        s = next_s
        if e%1 == 0:
            path.append(s)
    visualize(env,agent,path,value_function=True)


print('Finished')
print(agent.Qs)
s = env.reset()
done = False
agent.epsilon = 0

path = []

while not done:
    a = agent.choose_action(s)
    ns,r,done = env.step(a)
    path.append(s)
    s = ns
    print(path)
path.append(s)
print(path)
visualize(env,agent,path,value_function=True)


   
