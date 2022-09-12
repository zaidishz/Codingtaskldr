data = open('/Users/macbook/Desktop/Codingldr/day1.txt', 'r', encoding='utf-8').read().splitlines()
#Split a string into a list where each line is a list item
measurements = [int(x) for x in data]
#coversion to int
increases = sum(x < y for x, y in zip(measurements, measurements[1:]))
print(increases)
