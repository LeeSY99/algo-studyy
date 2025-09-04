N,M, K = map(int, input().split())

grid = [[0]*(M+1)]
for _ in range(N):
    grid.append([0] + list(input()))

a_sum = [[0]*(M+1) for _ in range(N+1)]
b_sum = [[0]*(M+1) for _ in range(N+1)]
c_sum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if grid[i][j] == 'a':
            a_sum[i][j] = a_sum[i-1][j] + a_sum[i][j-1] - a_sum[i-1][j-1] + 1
            b_sum[i][j] = b_sum[i-1][j] + b_sum[i][j-1] - b_sum[i-1][j-1]
            c_sum[i][j] = c_sum[i-1][j] + c_sum[i][j-1] - c_sum[i-1][j-1]

        elif grid[i][j] == 'b':
            a_sum[i][j] = a_sum[i-1][j] + a_sum[i][j-1] - a_sum[i-1][j-1]
            b_sum[i][j] = b_sum[i-1][j] + b_sum[i][j-1] - b_sum[i-1][j-1] + 1
            c_sum[i][j] = c_sum[i-1][j] + c_sum[i][j-1] - c_sum[i-1][j-1]
        else:
            a_sum[i][j] = a_sum[i-1][j] + a_sum[i][j-1] - a_sum[i-1][j-1]
            b_sum[i][j] = b_sum[i-1][j] + b_sum[i][j-1] - b_sum[i-1][j-1] 
            c_sum[i][j] = c_sum[i-1][j] + c_sum[i][j-1] - c_sum[i-1][j-1] + 1

def return_value(r1,c1,r2,c2):
    a_val = a_sum[r2][c2] - a_sum[r1-1][c2] - a_sum[r2][c1-1] + a_sum[r1-1][c1-1]
    b_val = b_sum[r2][c2] - b_sum[r1-1][c2] - b_sum[r2][c1-1] + b_sum[r1-1][c1-1]
    c_val = c_sum[r2][c2] - c_sum[r1-1][c2] - c_sum[r2][c1-1] + c_sum[r1-1][c1-1]
    print(a_val, b_val, c_val)

for _ in range(K):
    r1,c1,r2,c2 = map(int, input().split())
    return_value(r1,c1,r2,c2)
    
            
