n, m, c = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

choose = []
ans = 0
def backtrack(count):
    global choose
    global ans
    if count == n:
        if sum(choose) == 1 and 2*m >= n:
            val_sum = check1(choose)
            ans = max(ans, val_sum)
            
        elif sum(choose) == 2:
            val_sum = check2(choose)
            ans = max(ans, val_sum)
        return

    for i in range(2):
        choose.append(i)
        backtrack(count+1)
        choose.pop()

def check2(arr):
    for i in range(n):
        if arr[i] == 1:
            line1 = room[i]
            break
    for i in range(n-1, -1, -1):
        if arr[i] == 1:
            line2 = room[i]
            break
    result1, result2 = 0,0
    for i in range(n-m+1):
        weight1 = 0
        value1 = 0
        for k in range(m):
            weight1 += line1[i+k]
            if weight1 <= c:
                value1 += line1[i+k]**2   
        result1 = max(result1, value1)  

    for i in range(n-m+1):
        weight2 = 0
        value2 = 0
        for k in range(m):
            weight2 += line2[i+k]
            if weight2 <=c:
                value2 += line2[i+k]**2
        result2 = max(result2, value2)

    return result1 + result2    

def check1(arr):
    for i in range(n):
        if arr[i] == 1:
            line = room[i]
            break
    result = 0
    for i in range(n-m+1):
        for j in range(i+m,n-m+1):
            weight1, weight2 = 0, 0
            value1, value2 = 0, 0
            for k in range(m):
                weight1+=line[i+k]
                if weight1 <= c:
                    value1 += line[i+k]**2

                weight2 += line[j+k]
                if weight2 <= c:
                    value2 += line[j+k]**2
            result = max(result, value1 + value2)
    return result

backtrack(0)
print(ans) 