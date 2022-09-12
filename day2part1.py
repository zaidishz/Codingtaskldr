data = open('/Users/macbook/Desktop/Codingldr/day2.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
command = [(x[0], int(x[1])) for x in data]

horizontal, depth = 0, 0

for cmd, val in command:
    if cmd == 'forward':
        horizontal += val
    elif cmd == 'down':
        depth += val
    elif cmd == 'up':
        depth -= val
    else:
        raise ValueError('Invalid command')

print(horizontal * depth)
