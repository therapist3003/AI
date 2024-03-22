import matplotlib.pyplot as plt
def traingular(x,a,b,c):
    term1=(x-a)/(b-a)
    term2=(c-x)/(c-b)
    return max(min(term1,term2),0)
def trapezoidal(x,a,b,c,d):
    term1=(x-a)/(b-a)
    term2=(d-x)/(d-c)
    return max(min(term1,term2,1),0)
membership_values = {
  "nm": [31, 61, 95],
  "ns": [61, 95, 127],
  "ze": [95, 127, 159],
  "ps": [127, 159, 191],
  "pm": [159, 191, 223],
  "nl": [0, 0, 31, 61],
  "pl": [191, 223, 255, 255],
}

rules = [["nl", "ze", "pl"],
         ["ze", "nl", "pl"],
         ["nm", "ze", "pm"],
         ["ns", "ps", "ps"],
         ["ps", "ns", "ns"],
         ["pl", "ze", "nl"],
         ["ze", "ns", "ps"],
         ["ze", "nm", "pm"]]

speed=int(input("Enter the input speed value :- "))
accelaration=int(input("Enter the input accelaration value :- "))
for label in membership_values:
    if len(membership_values[label]) == 4:
      plt.plot(membership_values[label], [0, 1, 1, 0], label=label)
    else:
      plt.plot(membership_values[label], [0, 1, 0], label=label) 
plt.xlabel("throttle control")
plt.ylabel("membership value")

valid_rules=[]
for rule in rules:
    if membership_values[rule[0]][0]<=speed and speed<=membership_values[rule[0]][-1] and membership_values[rule[1]][0]<=accelaration and accelaration<=membership_values[rule[1]][-1]:
        valid_rules.append(rule)
fuzzy_triplets=[]
x=[speed,accelaration]
for v_rule in valid_rules:
    fuzz=[]
    for j in range(len(v_rule)-1):
        if len(membership_values[v_rule[j]])==3:
            fuzz.append(traingular(x[j],membership_values[v_rule[j]][0],membership_values[v_rule[j]][1],membership_values[v_rule[j]][2]))
        elif len(membership_values[v_rule[j]])==4:
            fuzz.append(trapezoidal(x[j],membership_values[v_rule[j]][0],membership_values[v_rule[j]][1],membership_values[v_rule[j]][2],membership_values[v_rule[j]][3]))
    fuzzy_triplets.append(min(fuzz))
fuzzy_op_value=max(fuzzy_triplets)    
def cal_centroid(l):
    return (l[0]+l[-1])/2
def area_triangle(h,l):
    a,b,c=l[0],l[1],l[2]
    x1=h*(b-a)+a
    x2=c-h*(c-b)
    d1=(c-a)
    d2=x2-x1
    plt.plot([x1,x2],[fuzzy_op_value,fuzzy_op_value])
    area=(0.5)*h*(d1+d2)
    return area

def area_trapezoid(h,l):
    a,b,c,d=l[0],l[1],l[2],l[3]
    x1=a+(b-a)*h
    x2=d-(d-c)*h
    d1=x2-x1
    d2=d-a
    plt.plot([x1,x2],[fuzzy_op_value,fuzzy_op_value])
    area=0.5*h*(d1+d2)
    return area
sum_cent_area,sum_area=0,0
for v_rule in valid_rules:
    c=cal_centroid(membership_values[v_rule[-1]])
    if len(membership_values[v_rule[-1]])==3:
        ar=area_triangle(fuzzy_op_value,membership_values[v_rule[-1]])
    elif len(membership_values[v_rule[-1]])==4:
        ar=area_trapezoid(fuzzy_op_value,membership_values[v_rule[-1]])
    sum_cent_area+=(c*ar)
    sum_area+=ar
output_value=sum_cent_area/sum_area
print("Output Value is ",output_value)

plt.legend()
plt.show()