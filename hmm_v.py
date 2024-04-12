import sys
n=list(input("Enter the states (excluding start state)  :- ").split())
poss_ip=list(input("Enter the possible inputs in each state :- ").split())
poss_prob={}
for i in n:
    temp={}
    for j in poss_ip:
        x=float(input(f"Enter the probability for {j} in state {i} :- "))
        temp[j]=x
    if sum(temp.values())==1:
        poss_prob[i]=temp
    else:
        print("Invalid Input")
        print("Error")
        sys.exit(0)
    
    
n.insert(0,"S")
tpm={}
for i in n:
    temp1={}
    for j in n:
        val=float(input(f'Enter the probability value of P[{i}][{j}] :- '))
        temp1[j]=val
    if sum(temp1.values())==1:
        tpm[i]=temp1
    else:
        print("Invalid Input")
        print("Error")
        sys.exit(0)
    
print(n)
print(poss_ip)
print(poss_prob)
for i in tpm.keys():
    print(i,':',tpm[i])

sequence=input("Enter the input sequence for which prob vakue is to be found : ")
res_table={}
t={}
for j in range(1,len(n)):
    t[n[j]]=[tpm['S'][n[j]]*poss_prob[n[j]][sequence[0]],n[j]]
res_table[0]=t
for i in range(1,len(sequence)):
    t={}
    for j in range(1,len(n)):
        val=[]
        for k in range(1,len(n)):
            val.append(((res_table[i-1][n[k]][0])*(tpm[n[k]][n[j]])*(poss_prob[n[j]][sequence[i]])))
        t[n[j]]=[max(val),n[1+val.index(max(val))]]
    res_table[i]=t
    
for i in res_table.keys():
    print(i,':',res_table[i])
res_sequence=""
st=[]
for i in range(1,len(n)):
    st.append([res_table[len(res_table)-1][n[i]][0],res_table[len(res_table)-1][n[i]][1]])
start=max(st,key=lambda x:x[0])[1]
res_sequence+=start
keys_tb=list(res_table.keys())[::-1]
for i in keys_tb[1:]:
    res_sequence+=res_table[i][start][1]
    start=res_table[i][start][1]
res_sequence=res_sequence[::-1]
print("the possible state sequence for the given output S is : ",res_sequence)
 
