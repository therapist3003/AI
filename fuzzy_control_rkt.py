import matplotlib.pyplot as plt

def triangular_membership(x, a, b, c):
    val1 = (x-a)/(b-a)
    val2 = (c-x)/(c-b)

    return max(min(val1, val2), 0)

def trapezoid_membership(x, a, b, c, d):
    val1 = (x-a)/(b-a)
    val2 = (d-x)/(d-c)

    return max(min(val1, val2, 1), 0)

# Centroid of trapezium is midpoint of base
def centroid(x_vals_list):
    return (x_vals_list[0] + x_vals_list[-1])/2

def getTriangleArea(height, traingleCoords):
    a, b, c = traingleCoords

    x1 = height*(b-a) + a
    x2 = c - height*(c-b)

    top = c-a
    base = x2-x1

    plt.plot([x1,x2], [height, height])
    area = (0.5)*height*(base + top)

    return area

def getTrapezoidArea(height, trapezoidCoords):
    a, b, c, d = trapezoidCoords

    x1 = a + height*(b-a)
    x2 = d - height*(d-c)

    top = d-a
    base = x2-x1

    plt.plot([x1,x2], [height,height])
    area = (0.5)*height*(base + top)

    return area

# Common for two input attributes and output, since distribution is same
membership_vals = {"nl": [0, 0, 31, 61],
                    "nm": [31, 61, 95],
                    "ns": [61, 95, 127],
                    "ze": [95, 127, 159],
                    "ps": [127, 159, 191],
                    "pm": [159, 191, 223],
                    "pl": [191, 223, 255, 255]
                }
# Rule base. Each rule is of the form if rule[0] and rule[1] then rule[2]
rules = [["nl", "ze", "pl"],
         ["ze", "nl", "pl"],
         ["nm", "ze", "pm"],
         ["ns", "ps", "ps"],
         ["ps", "ns", "ns"],
         ["pl", "ze", "nl"],
         ["ze", "ns", "ps"],
         ["ze", "nm", "pm"]]

speed_diff = float(input('Enter speed difference: '))
acceleration = float(input('Enter acceleration: '))

# Plotting graph for throttle control
for category in membership_vals.keys():
    # Trapezoid curve case
    if len(membership_vals[category]) == 4:
        plt.plot(membership_vals[category], [0, 1, 1, 0], label=category)
    else:
        plt.plot(membership_vals[category], [0, 1, 0], label=category)

plt.xlabel('Throttle control')
plt.ylabel('Membership value')

# Checking for rules that match the input
applicable_rules = []
for rule in rules:
    # Change this if range excludes last element
    if speed_diff in range(membership_vals[rule[0]][0], membership_vals[rule[0]][-1]) and acceleration in range(membership_vals[rule[1]][0], membership_vals[rule[1]][-1]):
        applicable_rules.append(rule)

fuzzy_vals = []
input_attribute_vector = [speed_diff, acceleration]

for rule in applicable_rules:
    attrib_membership_vals = []

    # Iterating over each input attribute except the result
    for i in range(len(rule)-1):
        # Triangle case
        if len(membership_vals[rule[i]]) == 3:
            attrib_membership_vals.append(triangular_membership(input_attribute_vector[i], membership_vals[rule[i]][0], membership_vals[rule[i]][1], membership_vals[rule[i]][2]))
        # Trapezoid case
        elif len(membership_vals[rule[i]]) == 4:
            attrib_membership_vals.append(trapezoid_membership(input_attribute_vector[i], membership_vals[rule[i]][0], membership_vals[rule[i]][1], membership_vals[rule[i]][2], membership_vals[rule[i]][3]))

    # Taking fuzzy AND
    fuzzy_vals.append(min(attrib_membership_vals))

# Taking fuzzy OR for all rules
fuzzy_res_val = max(fuzzy_vals) # Fuzzified value

# By centroid method, defuzzified value = SUMM(Centroid * Area) / SUMM(Area)
summ_cent_area, summ_area = 0, 0

for rule in applicable_rules:
    centroid_val = centroid(membership_vals[rule[-1]])

    if len(membership_vals[rule[-1]]) == 3:
        area = getTriangleArea(fuzzy_res_val, membership_vals[rule[-1]])
    elif len(membership_vals[rule[-1]]) == 4:
        area = getTrapezoidArea(fuzzy_res_val, membership_vals[rule[-1]])
    
    summ_cent_area += (centroid_val*area)
    summ_area += area

defuzz_val = summ_cent_area / summ_area
print('Defuzzified value: ', defuzz_val)

plt.legend()
plt.show()