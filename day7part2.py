data = open("/Users/macbook/Desktop/Codingldr/day7.txt", encoding='utf-8').read()
df = list(map(int, data.split(',')))
p_min, p_max = min(df), max(df)
fuels = [sum(map(lambda x: abs(x - p) * (abs(x - p) + 1) // 2, df)) for p in range(p_min, p_max + 1)]
print(min(fuels))
