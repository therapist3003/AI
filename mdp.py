states=list(input("Enter the states of the MDP space separated :- ").split())
actions=list(input("Enter the actions performed in each state space separated :- ").split())
discount=float(input("Enter the discount factor :- "))
reward={}
for i in range(len(states)):
    reward[states[i]]=int(input(f"Enter the reward value for state {states[i]} :-   "))

prob_values={}
for i in states:
    t={}
    for j in actions:
        t1={}
        while sum(t1.values())<1:
            state_n=input(f"Enter the state reached ON {j} from {i} :- ")
            prob_val=float(input(f"Enter the probability of the value P({state_n}|{i},{j}) :- "))
            t1[state_n]=prob_val
        t[j]=t1
    prob_values[i]=t
print(prob_values)

# prob_values={'PU': {'A': {'PU': 0.5, 'PF': 0.5}, 
#         'S': {'PU': 1.0}}, 
#  'PF': {'A': {'PF': 1.0}, 
#         'S': {'PU': 0.5, 'RF': 0.5}}, 
#  'RF': {'A': {'RF': 1.0},
#         'S': {'RU': 0.5, 'RF': 0.5}}, 
#  'RU': {'A': {'PU': 0.5, 'PF': 0.5}, 
#         'S': {'RU': 0.5, 'PU': 0.5}}}

def close(a,b,thresh):
    for key in a:
        if abs(a[key] - b[key]) >= thresh:
            return False
    return True

print(reward)
res_rewards={}
pass_no=0
res_rewards[pass_no]=reward
pass_no+=1
while True:#tolerance value 0.05 maintained , if wanted this third value can be changed
    x={}
    for i in states:
        t2={}
        for j in prob_values[i]:
            val=0
            for k in prob_values[i][j]:
                val+=prob_values[i][j][k]*res_rewards[pass_no-1][k]
            t2[j]=val
        x[i]=reward[i]+discount*max(t2.values())
    res_rewards[pass_no]=x
    if close(res_rewards[pass_no],res_rewards[pass_no-1],0.05):
        break
    pass_no+=1
for i in res_rewards:
    print(i,":",res_rewards[i])