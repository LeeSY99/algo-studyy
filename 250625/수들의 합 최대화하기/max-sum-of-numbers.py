n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
index = []

def backtrack(count):
    if count == n:
        print_ans()
        return
    
    for i in range(n):
        if visited[i] == 1:
            continue
        
        visited[i]=1
        index.append(i)
        backtrack(count+1)

        visited[i] = 0
        index.pop()

ans = 0
def print_ans():
    global ans
    result = 0
    for i in range(n):
        result += grid[i][index[i]]
    ans = max(ans, result)
    

backtrack(0)
print(ans)