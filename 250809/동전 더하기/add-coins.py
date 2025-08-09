n, k = map(int, input().split())

coins = []
for _ in range(n):
    c = int(input())
    coins.append(c)

count = 0
for coin in coins[::-1]:
    count += k//coin
    k = k%coin

print(count)