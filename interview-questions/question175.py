"""
    Create a function to run a markov chain for n iterations
    given a starting state and a matrix which models the markov 
    process
"""
from random import random
def fun(start_state,markov_chain,iterations):
    state_dict = {}
    cur_state = start_state
    for _ in range(iterations):
        probability = random() 
        lowest_probability = float("inf")
        for P in markov_chain:
            if(P[0] == cur_state):
                if(probability <= P[2] and P[2] < lowest_probability):
                    new_state = P[1]
                    lowest_probability = P[2]
        cur_state = new_state
        state_dict[cur_state] = state_dict.get(cur_state,0) + 1
    return state_dict
if __name__ == "__main__":
    chain = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]    
    print(fun("a",chain,5000))
