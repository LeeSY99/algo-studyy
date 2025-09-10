n, k = map(int, input().split())
candy = [0] * 1000001
for _ in range(n):
    a, x = map(int, input().split())
    candy[x] += a

sum_val = sum(candy[1: 1+k+k +1])
ans = sum_val
for c in range(2+k, 1000001 - k):
    i = c-k
    j = c+k
    sum_val -= candy[i-1]
    sum_val += candy[j]
    ans = max(ans, sum_val)
    


print(ans)


