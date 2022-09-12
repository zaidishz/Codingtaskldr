data = open('/Users/macbook/Desktop/Codingldr/day1.txt', 'r', encoding='utf-8').read().splitlines()
measurements = [int(x) for x in data]
#  measurements[i] + measurements[i+1] + measurements[i+2] < depths[i+1] + measurements[i+2] + measurements[i+3] has the same resuts as comparing: measurements[i] < measurements[i+3]
increases = sum(x < y for x, y in zip(measurements, measurements[3:]))
print(increases)