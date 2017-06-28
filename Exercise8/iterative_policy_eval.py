#!/usr/bin/python3

def initialize(no_states):
    
    Vs = ['0'] * no_states    
    
    no_actions = 4
    
    actions = [1/no_actions for _ in range(no_actions)] # up, right, down, left    
    
    pi_sa = [actions] * no_states
    
    return Vs, pi_sa
    
def full_policy_evaluation_backup(Vs, pi_sa):
    
    return Vs

def evaluate(Vs, pi_sa, sigma):
    k = 0
    delta = 0
    
    while delta < sigma:
        delta = 0
        
        for state in Vs:
            temp = Vs
            Vs = 0
            sigma = 0
            k += 1
    
    return k



####
NO_STATES = 16
SIGMA = 0.2

Vs, pi_sa = initialize(NO_STATES)
k = evaluate(Vs, pi_sa, SIGMA)

print (k)
print (Vs)
#final_k = evaluate(V)