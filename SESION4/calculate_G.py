import numpy as np
GAMMA = 1

def calculate_return(sequence_states_rewards):
    G = 0
    ssr = sequence_states_rewards
    seq_states_returns = {ssr[-1][0]:[G]}#[(ssr[-1][0],G)]
    #just_returns = [G]
    visited_states = [ssr[-1][0]]
    for s,r in reversed(ssr[:-1]):
            if s not in visited_states:
                seq_states_returns[s] = []
                visited_states.append(s)
            G = r + GAMMA*G
            seq_states_returns[s].append(G)
            #seq_states_returns.append((s,G))
            #just_returns.append(G)
    #seq_states_returns.reverse()
    #just_returns.reverse()
    for s in seq_states_returns:
        seq_states_returns[s] = np.mean(seq_states_returns[s])
        
    #print('visited_states',visited_states)
    return seq_states_returns#,just_returns
