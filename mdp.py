def close(a, b, threshold):
    for key in a:
        if abs(a[key] - b[key]) >= threshold:
            return False
    return True

states = input("Enter the states (space-separated): ").split()
actions = input("Enter the actions at each state (space-separated): ").split()

discount_factor = float(input("Enter discount factor: "))

reward_dict={}
for i in range(len(states)):
    reward_dict[states[i]]=int(input('Enter the reward at state ' + states[i] + ' : '))

# Key - State, Value - Dict (Key - Action Value - Dict (Key - To_state, Value - Probability) )
prob_values={}
for i in states:
    # Key - Action , Value - Dict (Key - To_state, Value - Probability)
    transition_probs =  {}
    for j in actions:
        # Key - To_state, Value - Probability
        to_state_probabs={}
        while sum(to_state_probabs.values())<1:
            to_state = input('Enter the state reached from ' + i + ' by ACTION ' + j + ': ')
            probab_val = float(input('Enter probability: '))
            to_state_probabs[to_state] = probab_val
        transition_probs[j] = to_state_probabs
    prob_values[i] = transition_probs

print(prob_values)

# prob_values={'PU': {'A': {'PU': 0.5, 'PF': 0.5}, 
#         'S': {'PU': 1.0}}, 
#  'PF': {'A': {'PF': 1.0}, 
#         'S': {'PU': 0.5, 'RF': 0.5}}, 
#  'RF': {'A': {'RF': 1.0},
#         'S': {'RU': 0.5, 'RF': 0.5}}, 
#  'RU': {'A': {'PU': 0.5, 'PF': 0.5}, 
#         'S': {'RU': 0.5, 'PU': 0.5}}}

print('Undiscounted rewards: ')
print(reward_dict)

# Value Iteration Method
# Key - State, Value - Discounted reward at each iteration
res_rewards = {}
iter_no = 0
# Iteration 0
res_rewards[iter_no] = reward_dict

iter_no += 1

while True:
    # Current iteration rewards
    curr_rewards = {}
    for state in states:
        # Temporary reward values for each action (to find max)
        temp_reward_dict = {}
        for action in prob_values[state]:
            val = 0
            for probab in prob_values[state][action]:
                val += prob_values[state][action][probab] * res_rewards[iter_no-1][probab]
            temp_reward_dict[action] = val
        curr_rewards[state] = reward_dict[state] + discount_factor*max(temp_reward_dict.values())

    res_rewards[iter_no] = curr_rewards

    if close(res_rewards[iter_no], res_rewards[iter_no-1], 0.05):
        break
    iter_no += 1

for iter in res_rewards:
    print('Iteration ', iter,": ", res_rewards[iter])