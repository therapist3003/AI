# Randomly generate problem
import random
max_city_number = 8
Gs = []
for NN in range(2,max_city_number):
Gs.append([[random.randint(1,10) for e in range(NN+1)] for e in range(NN+1)])
# Problem state representation: Tree structure
class node(object):
def __init__(self,number=None):
self.pre = None
self.no = number
self.label = []
self.child = []
self.cost = None
def add_child(self,number):
tmp_node = node(number=number)
tmp_node.pre = self
tmp_node.label=[i for i in self.label]
tmp_node.label.append(number)
tmp_node.cost= get_bound(tmp_node.label)
self.child.append(tmp_node)
# Evaluate Function for A Algorithm
def get_bound(label):
f = 0
for i in range(0,len(label)-1):
f = f+graph[label[i]-1][label[i+1]-1]
remain = city.difference(set(label))
remain = list(remain)
remain.append(label[-1])
for i in remain:
f = f+min_bound[i-1]
if len(remain)==2:
f=0
label.append(remain[0])
label.append(1)
for i in range(0,len(label)-1):
f = f+graph[label[i]-1][label[i+1]-1]
return f
# Evaluate Function for Best-first Algorithm
def get_bound(label):
f = 0
remain = city.difference(set(label))
remain = list(remain)
remain.append(label[-1])
for i in remain:
f = f+min_bound[i-1]
if len(remain)==2:
f=0
label.append(remain[0])
label.append(1)
for i in range(0,len(label)-1):
f = f+graph[label[i]-1][label[i+1]-1]
return f
# Evaluate Function for Depth-first/Breadth-first Algorithm
def get_bound(label,n_city):
f = 0
for i in range(0,len(label)-1):
f = f+graph[label[i]-1][label[i+1]-1]
if len(label)==len(graph):
f = f+graph[label[-1]-1][0]
return f
# Effective Branch Number calculation (Newton's Method)
def f(N,d,x):
return (x**(d+1) - (N+1)*x + N)**2
def df(N,d,x):
return 2*f(N,d,x)*((d+1)*x**d-(N+1))
def ddf(N,d,x):
return 2*df(N,d,x)*((d+1)*x**d-(N+1))+2*f(N,d,x)*((d+1)*d*x**(d-1))
def solve(N,d):
x = 1.9
delta = 1.0
count = 0
while abs(delta)>0.000001 and count<10000:
delta = df(N,d,x)/(ddf(N,d,x)+0.00001)
x = x - delta
count = count + 1
return x
# EXPERIMENT1/2: 
# Search for GOAL (for A algorithm/Best-first Algorithm)
tree = node(number=1)
tree.label.append(1)
tree.cost=0
for i in range(len(Gs)):
print("----------i=%d------------"%i)
graph = Gs[i]
NN = len(graph)
for idx in range(NN):
graph[idx][idx] = float('inf')
city = range(1,len(graph)+1)
city = set(city)
min_bound = [min(graph[i]) for i in range(len(graph))]
tree = node(number=1)
tree.label.append(1)
tree.cost=0
visit=[]
visit.append(tree)
count = 0
fcnt = 0
ans = 0
while len(visit)>0:
N = visit[0]
if len(N.label)==(len(city)-2):
fcnt = fcnt+1
del(visit[0])
count = count+1
child_list = set(city).difference(set(N.label))
if len(child_list)==0:
ans = 1
break
for c in child_list:
N.add_child(number=c)
tmp = N.child
for i in tmp:
visit.append(i)
visit = sorted(visit,key= lambda x:x.cost)
if ans==1:
print("RESULT:",N.label,N.cost)
b = solve(count,NN-2)
print("d=%d ,N= %d ,  b*=%f"%(NN-2,count,b))
print("ROUTEs: %d"%(fcnt))
resultsA.append((NN-2,count,b))
else:
print("FAILED")
# EXPERIMENT3: 
# Search for GOAL (for Depth-first algorithm)
tree = node(number=1)
tree.label.append(1)
tree.cost=0
for i in range(len(Gs)):
print("----------i=%d------------"%i)
graph = Gs[i]
NN = len(graph)
for idx in range(NN):
graph[idx][idx] = float('inf')
city = range(1,len(graph)+1)
city = set(city)
tree = node(number=1,n_city=len(city))
tree.label.append(1)
tree.cost=0
visit=[]
paths = []
count = 0
fcnt = 0
visit.append(tree)
while len(visit)>0:
if len(visit)==0:
break
N = visit.pop()
if len(N.label)==(len(graph)+1):
paths.append(N)
fcnt = fcnt+1
paths=sorted(paths,key= lambda x:x.cost)
count = count+1
child_list = set(city).difference(set(N.label))
if len(child_list)==0:
continue
for c in child_list:
N.add_child(number=c)
tmp = N.child
for i in tmp:
visit.append(i)
print("RESULT:",paths[0].label,paths[0].cost)
print("d=%d ,N= %d ,  b*=%f"%(NN-2,count,solve(count,NN-2)))
print("ROUTEs:%d"%(fcnt))
# EXPERIMENT4: 
# Search for GOAL (for Breadth-first algorithm)
tree = node(number=1)
tree.label.append(1)
tree.cost=0
for i in range(len(Gs)):
print("----------i=%d------------"%i)
graph = Gs[i]
NN = len(graph)
for idx in range(NN):
graph[idx][idx] = float('inf')
city = range(1,len(graph)+1)
city = set(city)
tree = node(number=1,n_city=len(city))
tree.label.append(1)
tree.cost=0
visit=[]
paths = []
count = 0
fcnt = 0
visit.append(tree)
while len(visit)>0:
if len(visit)==0:
break
N = visit[0]
del(visit[0])
if len(N.label)==(len(graph)+1):
paths.append(N)
fcnt = fcnt+1
paths=sorted(paths,key= lambda x:x.cost)
count = count+1
child_list = set(city).difference(set(N.label))
if len(child_list)==0:
continue
for c in child_list:
N.add_child(number=c)
tmp = N.child
for i in tmp:
visit.append(i)
print("RESULT:",paths[0].label,paths[0].cost)
print("d=%d ,N= %d ,  b*=%f"%(NN-2,count,solve(count,NN-2)))
print("ROUTEs:%d"%(fcnt))