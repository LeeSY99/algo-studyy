n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def down(arr):
    for j in range(n):
        col = [arr[i][j] for i in range(n)]
        col = [num for num in col if num != 0]
        new_col = [0]*(n-len(col)) 
        new_col += col
        for i in range(n):
            arr[i][j] = new_col[i]
    return arr
    
def turn(arr):
    new_arr = [[0]*n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            new_arr[i][j] = arr[n-j-1][i]
    new_arr = down(new_arr)
    return new_arr

def boom():
    for j in range(n):
        now = numbers_2d[0][j]
        start = 0
        end = 0
        for i in range(1, n):
            if numbers_2d[i][j] == now:
                end = i
            else:
                if end-start+1 >= m:
                    for k in range(start,end+1):
                        numbers_2d[k][j] = 0
                start = i
                end = i
                now = numbers_2d[i][j]
        if end-start+1 >= m:
            for k in range(start,end+1):
                numbers_2d[k][j] = 0
            start = i
            end = i    
            now = numbers_2d[i][j]

for _ in range(k):
    boom()            
    numbers_2d=down(numbers_2d)
    numbers_2d=turn(numbers_2d)
boom()


# for a in numbers_2d:
#     print(*a)
count = 0
for row in numbers_2d:
    for num in row:
        if num != 0:
            count+=1

print(count)