n = int(input())
nums = [int(input()) for _ in range(n)]

prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = (prefix[i-1] + nums[i-1]) % 7

first = [-1] * 7
last  = [-1] * 7

for i in range(n+1):
    r = prefix[i]
    if first[r] == -1:
        first[r] = i
    last[r] = i

ans = 0
for m in range(7):
    if first[m] != -1 and last[m] != -1:
        ans = max(ans, last[m] - first[m])

print(ans)
