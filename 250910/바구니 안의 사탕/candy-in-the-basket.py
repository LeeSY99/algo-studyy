n, k = map(int, input().split())
candy = [0] * 1000001
for _ in range(n):
    a, x = map(int, input().split())
    candy[x] += a

j = 2 * k
sum_val = sum(candy[:j+1])
ans = sum_val
for i in range(1000001):
    sum_val -= candy[i]
    j += 1
    sum_val += candy[j]
    ans = max(ans, sum_val)
    if j == 100000:
        break

print(ans)


