n = int(input())

bag = [float('inf')] * (n+1)
bag[0] = 0
if n>=5:
    bag[5] = 1

for i in range(3, n+1):
    if bag[i-3] != float('inf'):
        bag[i] = min(bag[i], bag[i-3]+1)

    if bag[i-5] != float('inf'):
        bag[i] = min(bag[i], bag[i-5]+1)
# print(bag)
print(bag[n] if bag[n] != float('inf') else -1)
