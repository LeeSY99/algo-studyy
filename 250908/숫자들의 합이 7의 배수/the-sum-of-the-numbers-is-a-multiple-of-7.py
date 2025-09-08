n = int(input())
nums = [int(input()) for _ in range(n)]
##나머지가 같으면 뺏을때 k의 배수가 된다->
## 그래서 prefix_sum에서 나머지가 m인 처음 나타난 인덱스와 가장 마지막에 나온 인덱스를
## 구해서 빼면 구간이 나온다
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
