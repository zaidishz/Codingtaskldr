#Part1
data = open('/Users/macbook/Desktop/Codingldr/day3.txt', 'r', encoding='utf-8').read().splitlines()

x = len(data[0])
#print(x)
gamma = 0
epsilon = 0

for n in range(x):
    count0 = sum(1 for a in data if a[n] == '0')
    count1 = len(data) - count0
    gamma *= 2
    epsilon *= 2
    if count0 < count1:
        gamma += 1
    else:
        epsilon += 1

print('power consumption:', gamma * epsilon)

#Part2 

#Oxygen rating
def most_common(lst, position):
    count0 = sum(1 for x in lst if x[position] == '0')
    count1 = len(lst) - count0
    return '0' if count0 > count1 else '1'


def keep_most_common(d, position):
    v = most_common(d, position)
    return [x for x in d if x[position] == v]


lst = data.copy()
for i in range(x):
    if len(lst) <= 1:
        break
    lst = keep_most_common(lst, i)
# converting a binary to integer with int()
oxygen = int(lst[0], 2)
print("oxygen", oxygen)


#CO2 rating
def least_common(lst, position):
    count0 = sum(1 for x in lst if x[position] == '0')
    count1 = len(lst) - count0
    return '0' if count0 <= count1 else '1'


def keep_least_common(d, position):
    v = least_common(d, position)
    return [x for x in d if x[position] == v]


lst = data.copy()
for i in range(x):
    if len(lst) <= 1:
        break
    lst = keep_least_common(lst, i)

co2 = int(lst[0], 2)
print("co2", co2)

#Life support rating
print("life support rating", co2 * oxygen)
