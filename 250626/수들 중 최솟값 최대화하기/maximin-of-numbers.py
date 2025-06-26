n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

selected_index = []
visited = [0] * (n)

def backtrack(count):
    if count == n:
        calc()
        return

    for i in range(n):
        if visited[i] == 1:
            continue
        selected_index.append(i)
        visited[i] = 1
        backtrack(count+1)
        
        visited[i] = 0
        selected_index.pop()

import sys
ans = 0
def calc():
    global ans
    result = sys.maxsize
    for i in range(n):
        result = min(result, nums[i][selected_index[i]])
    ans = max(ans, result)

backtrack(0)
print(ans)

    