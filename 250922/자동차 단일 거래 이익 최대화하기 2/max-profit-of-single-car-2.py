n = int(input())
price = list(map(int, input().split()))

buy = price[0]
benefit = 0

for i in range(1,n):
    if price[i] < buy:
        buy = price[i]
    else:
        benefit = max(benefit, price[i] - buy)
# print(buy)
print(benefit)
    