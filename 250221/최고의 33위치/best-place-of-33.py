n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def in_range(i,j):
    return 0 <= i <= n-3 and 0 <= j <=n-3

max_sum=0
for i in range(n):
    for j in range(n):
        if in_range(i,j):
            coin=0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    coin+=grid[k][l]
            max_sum=max(max_sum,coin)

print(max_sum)