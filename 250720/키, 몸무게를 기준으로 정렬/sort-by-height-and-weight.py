n = int(input())

info = []
for _ in range(n):
    name, height, weight = input().split()
    height = int(height)
    weight = int(weight)

    info.append((name,height,weight))

info.sort(key = lambda x: (x[1],-x[2]))

for name,height,weight in info:
    print(name, height, weight)
