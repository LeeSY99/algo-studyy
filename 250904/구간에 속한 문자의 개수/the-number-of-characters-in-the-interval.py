N,M, K = map(int, input().split())

grid = [[0]*(M+1) for _ in range(N+1)]


for i in range(1,N+1):
    row = input()
    for j in range(1,M+1):
        if row[j-1] == 'a':
            grid[i][j] = 1
        elif row[j-1] =='b':
            grid[i][j] = 2
        else:
            grid[i][j] = 3

prefix_sum = [[[0] * (M+1) for _ in range(N+1)] for _ in range(4)]

for c in range(1,4):
    for i in range(1,N+1):
        for j in range(1,M+1):
            add_val = 0
            if grid[i][j] == c:
                add_val = 1
                
            prefix_sum[c][i][j] = prefix_sum[c][i-1][j] + prefix_sum[c][i][j-1] - prefix_sum[c][i-1][j-1] + add_val

def return_value(c,r1,c1,r2,c2):
    return prefix_sum[c][r2][c2] - prefix_sum[c][r1-1][c2] - prefix_sum[c][r2][c1-1] + prefix_sum[c][r1-1][c1-1]


for _ in range(K):
    r1,c1,r2,c2 = map(int, input().split())
    print(return_value(1,r1,c1,r2,c2),return_value(2,r1,c1,r2,c2),return_value(3,r1,c1,r2,c2))
    
            
