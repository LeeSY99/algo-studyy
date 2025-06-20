n, m, c = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

def get_max_value(arr):
    max_val = 0
    def backtrack(index, weight, value):
        nonlocal max_val
        if weight > c:
            return
        if index == m:
            max_val = max(max_val, value)
            return
        
        backtrack(index+1, weight+arr[index], value+ arr[index] **2)
        backtrack(index+1, weight, value)
    backtrack(0,0,0)
    return max_val

max_result = 0
for i in range(n): #한 행에 2명 도둑
    for j in range(n-m+1):
        part1 = room[i][j:j+m]
        val1 = get_max_value(part1)
        for k in range(j+m, n-m+1):
            part2 = room[i][k:k+m]
            val2 = get_max_value(part2)
            max_result=max(max_result, val1+val2)

for i in range(n):
    for j in range(n-m+1):
        part1 = room[i][j:j+m]
        val1 = get_max_value(part1)
        for k in range(i+1, n):
            for l in range(n-m+1):
                part2 = room[k][l:l+m]
                val2 = get_max_value(part2)
                max_result = max(max_result, val1+val2)

print(max_result)
