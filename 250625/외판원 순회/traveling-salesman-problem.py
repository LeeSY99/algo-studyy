n = int(input())

aij = [list(map(int, input().split())) for _ in range(n)]

visited = [1] + [0] * (n-1)
selected_index = [0]

def backtrack(count):
    if count == n:
        calc()
        return

    for i in range(1,n):
        if visited[i] == 1:
            continue
        
        visited[i] =1
        selected_index.append(i)
        backtrack(count+1)

        visited[i] = 0
        selected_index.pop()

import sys
ans = sys.maxsize
def calc():
    global ans
    result = 0
    selected_index.append(0)
    for a in range(n):
        i, j = selected_index[a], selected_index[a+1]
        if aij[i][j] == 0:
            selected_index.pop()
            return
        result += aij[i][j]
    ans = min(ans, result)
    selected_index.pop()

backtrack(1)
print(ans)


        

