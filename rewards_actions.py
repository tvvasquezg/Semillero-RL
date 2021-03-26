import numpy as np

def get_reward(qs,action):
    return np.random.normal(qs[action],1)



def choose_action(Qs,epsilon=0.1):
    p = np.random.rand()

    if p < epsilon:
        return np.random.choice(len(Qs))
    else:
        return np.argmax(Qs)
