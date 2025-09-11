n,k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()
# print(arr)

j = 0
g1 = []
g2 = []
ans = 0
for i in range(n):
    if len(g1) <= len(g2):
        g1 = []
        now = g1
    else:
        g2 = []
        now = g2
    while j<n and arr[j] - arr[i] <= k:
        now.append(arr[j])
        j+=1

    ans = max(ans, len(g1) + len(g2))

print(ans)


