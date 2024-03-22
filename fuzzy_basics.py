#%%

class FuzzySet:
    def __init__(self, cardinality=0, elements=dict()):
        self.elements = elements
        self.cardinality = cardinality
        
    def union(self, set2):
        temp = {}
        
        for elem in self.elements.keys():
            if elem in set2.elements.keys():
                temp[elem] = max(self.elements[elem], set2.elements[elem])
            else:
                temp[elem] = self.elements[elem]
                
        for elem in set2.elements.keys():
            if elem not in temp.keys():
                temp[elem] = set2.elements[elem]
                
        return FuzzySet(len(temp), temp)
    
    def intersection(self, set2):
        temp = {}
        
        for elem in self.elements.keys():
            if elem in set2.elements.keys():
                temp[elem] = min(self.elements[elem], set2.elements[elem])
                
            else:
                temp[elem] = 0
                
        for elem in set2.elements.keys():
            if elem not in temp.keys():
                temp[elem] = 0
                
        return FuzzySet(len(temp), temp)
    
    def complement(self):
        temp = {}
        
        for elem in self.elements.keys():
            temp[elem] = 1 - self.elements[elem]
            
        return FuzzySet(len(temp), temp)
    
    def difference(self, set2):
        return self.intersection(set2.complement())
    
    def cartesian_product(self, set2):
        res = {}
        for i in self.elements.keys():
            for j in set2.elements.keys():
                res[(i,j)] = min(self.elements[i], set2.elements[j])
        
        return FuzzySet(len(res), res)        
    
    def display(self):
        for key in self.elements.keys():
            print('Element: ', key, ' Membership value: ', self.elements[key])
        
n = int(input('Enter no. of elements in set A: '))

A = {}
print('Enter elements of set A <space> membership_value :-')
for i in range(n):
    entry = input().split()
    element = int(entry[0])
    mem_val = float(entry[1])
    
    A[element] = mem_val
    
Fuzzy_A = FuzzySet(n, A)

print('Elements of A :-')
Fuzzy_A.display()

n = int(input('Enter no. of elements in set B: '))

B = {}
print('Enter elements of set B <space> membership_value :-')
for i in range(n):
    entry = input().split()
    element = int(entry[0])
    mem_val = float(entry[1])
    
    B[element] = mem_val
    
Fuzzy_B = FuzzySet(n, B)

print('\nElements of B :-')
Fuzzy_B.display()

print('\nUnion:-')
union_res = Fuzzy_A.union(Fuzzy_B)
union_res.display()

print('\nIntersection:-')
intersection_res = Fuzzy_A.intersection(Fuzzy_B)
intersection_res.display()

print('\nComplement A:-')
a_complement = Fuzzy_A.complement()
a_complement.display()

print('\nComplement B:-')
b_complement = Fuzzy_B.complement()
b_complement.display()

print('\nA - B :-')
a_diff_b = Fuzzy_A.difference(Fuzzy_B)
a_diff_b.display()

print('\nB - A :-')
b_diff_a = Fuzzy_B.difference(Fuzzy_A)
b_diff_a.display()


print('\nVerification of DeMorgan Laws:-')
print("(A U B)' = A' _intersect_ B'")

lhs = Fuzzy_A.union(Fuzzy_B).complement()
rhs = Fuzzy_A.complement().intersection(Fuzzy_B.complement())

print("\n(A U B)'")
lhs.display()

print("\nA' _intersect_ B'")
rhs.display()

print("\n(A _intersect_ B)' = A' U B'")

lhs = Fuzzy_A.intersection(Fuzzy_B).complement()
rhs = Fuzzy_A.complement().union(Fuzzy_B.complement())

print("\n(A _intersect_ B)'")
lhs.display()

print("\nA' U B'")
rhs.display()

cart_prod = Fuzzy_A.cartesian_product(Fuzzy_B)
print("\nA x B")
cart_prod.display()

#%%
def max_min(rel1, rel2):
    res_relation = FuzzyRelation()
    res_relation.domain1 = rel1.domain1
    res_relation.domain2 = rel2.domain2
    
    for x in rel1.domain1:
        for z in rel2.domain2:
            max_val = 0
            for y in rel1.domain2:
                if (x,y) in rel1.elements.keys():
                    a = rel1.elements[(x,y)]
                else:
                    a = 0
                if (y,z) in rel2.elements.keys():
                    b = rel2.elements[(y,z)]
                else:
                    b = 0
                
                min_val = min(a, b)
                max_val = max(min_val, max_val)
            
            res_relation.elements[(x,z)] = max_val
            
    return res_relation

class FuzzySet:
    def __init__(self):
        self.elements = {}

    def getInput(self):
        n = int(input('Enter no. of elements: '))
        
        print('Enter elements of the form (<element> <mem_val>):-')
        for i in range(n):
            entry = input().split()
            elem = int(entry[0])
            mem_val = float(entry[1])

            self.elements[elem] = mem_val

    def display(self):
        print(self.elements)
        
    def cartesian_product(self, set2):
        res_relation = FuzzyRelation()
        
        res_relation.domain1 = [key for key in self.elements.keys()]
        res_relation.domain2 = [key for key in set2.elements.keys()]
        
        for i in self.elements.keys():
            for j in set2.elements.keys():
                res_relation.elements[(i,j)] = min(self.elements[i], set2.elements[j])
        
        return res_relation
            
class FuzzyRelation:
    def __init__(self):
        self.elements = {}
        self.domain1 = []
        self.domain2 = []
    
    def getInput(self):
        self.domain1 = list(map(int, input('Enter space separated elements in domain 1: ').split()))
        self.domain2 = list(map(int, input('Enter space separated elements in domain 2: ').split()))
        
        n = int(input('Enter no. of elements in the relation: '))
        
        print('Enter x <space> y <space> membership_value :-')
        for i in range(n):
            entry = list(map(float, input().split()))
            x = int(entry[0])
            y = int(entry[1])
            mem_val = float(entry[2])
            self.elements[(x,y)] = mem_val
            
    def display(self):
        print(self.elements)
        
'''fset_A = FuzzySet()
print('Enter fuzzy set A:-')
fset_A.getInput()
print('Fuzzy Set A:-')
fset_A.display()

fset_B = FuzzySet()
print('Enter fuzzy set B:-')
fset_B.getInput()
print('Fuzzy Set B:-')
fset_B.display()

fset_C = FuzzySet()
print('Enter fuzzy set C:-')
fset_C.getInput()
print('Fuzzy Set C:-')
fset_C.display()'''

rel_R = FuzzyRelation()
rel_R.domain1 = [1,2]
rel_R.domain2 = [1,2]

rel_R.elements[(1,1)] = 0.7
rel_R.elements[(1,2)] = 0.6
rel_R.elements[(2,1)] = 0.8
rel_R.elements[(2,2)] = 0.3

print('Relation R:-')
rel_R.display()

rel_S = FuzzyRelation()
rel_S.domain1 = [1,2]
rel_S.domain2 = [1,2,3]

rel_S.elements[(1,1)] = 0.8
rel_S.elements[(1,2)] = 0.5
rel_S.elements[(1,3)] = 0.4
rel_S.elements[(2,1)] = 0.1
rel_S.elements[(2,2)] = 0.6
rel_S.elements[(2,3)] = 0.7

print('Relation S:-')
rel_S.display()

'''rel_S = fset_A.cartesian_product(fset_C)
print('Relation S:-')
rel_S.display()'''

composition_relation = max_min(rel_R, rel_S)
print('Max-min composition:-')
composition_relation.display()

#%%
from pyit2fls import IT2FS, trapezoid_mf, tri_mf
import numpy as np

# Trapezoid membership function
trapezoid = IT2FS(np.linspace(0.0, 1.0,100), trapezoid_mf, [0, 0.4, 0.6, 1.0, 1.0])
trapezoid.plot(filename='Trapezoid_plot')

triangle = IT2FS(np.linspace(0.0, 1.0,100), tri_mf, [0, 0.6, 1.0, 1.0])
triangle.plot(filename='triangle_plot')