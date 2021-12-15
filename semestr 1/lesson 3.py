with open("ikea.txt", 'r', encoding="utf-8") as f:
    data = list(map(lambda x: x.strip().split(), f.readlines()))

for line in data:
    print(*line)