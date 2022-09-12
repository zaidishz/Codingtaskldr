data = open('/Users/macbook/Desktop/Codingldr/day2.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
command = [(x[0], int(x[1])) for x in data]

aim, horizontal, depth = 0, 0, 0

for cmd, val in command:
    if cmd == 'forward':
        horizontal += val
        depth += val * aim
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val
    else:
        raise ValueError('Invalid command')

print(horizontal * depth)
