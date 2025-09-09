n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
ans = 0

for i in range(n):
    if arr[i] > k:
        break
    j = i+1
    while j<n and arr[i] + arr[j] <= k:
        j += 1
    ans += j - i -1

print(ans)
    