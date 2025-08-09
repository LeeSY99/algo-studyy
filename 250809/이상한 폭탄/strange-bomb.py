n, k = map(int, input().split())

arr = []
for _ in range(n):
    b = int(input())
    arr.append(b)

r = [0]* n

latest_index = dict()

for i in range(n-1,-1,-1):
    if arr[i] not in latest_index:
        r[i] = -1

    else:
        r[i] = latest_index[arr[i]]

    latest_index[arr[i]] = i

ans = -1
for i in range(n):
    if r[i] != -1 and r[i] - i <=k:
        ans = max(ans, arr[i])

print(ans)