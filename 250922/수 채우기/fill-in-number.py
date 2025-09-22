n = int(input())

ans = float('inf')
for i in range(1, n//5+1):
    if (n - 5*i) % 2 == 0:
        cnt = i
        remain = n - 5*i
        cnt += remain // 2
        ans = min(ans, cnt)


if ans == float('inf'):
    ans = -1

print(ans)