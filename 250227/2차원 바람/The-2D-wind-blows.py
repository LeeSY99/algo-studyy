n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

def wind_movd(r1,c1,r2,c2):

    #상단
    temp = a[r1][c1:c2+1]
    rest = temp.pop()
    index = 0
    for i in range(c1+1,c2+1):
        a[r1][i] = temp[index]
        index+=1

    #우측
    temp = [a[i][c2] for i in range(r1+1,r2+1)]
    rest2 = temp.pop()
    temp.insert(0,rest)
    rest=rest2
    index = 0
    for i in range(r1+1,r2+1):
        a[i][c2] = temp[index]
        index+=1

    #하단
    temp = a[r2][c1:c2]
    rest2 = temp.pop(0)
    temp.append(rest)
    rest=rest2
    index = 0
    for i in range(c1,c2):
        a[r2][i] = temp[index]
        index += 1

    #좌측
    temp = [a[i][c1] for i in range(r1,r2)]
    rest2 = temp.pop(0)
    temp.append(rest)
    rest=rest2
    index = 0
    for i in range(r1,r2):
        a[i][c1] = temp[index]
        index +=1

def in_range(r,c):
    return 0<=r <n and 0<=c <m

import copy
def change_avg(r1,c1,r2,c2):
    a2=copy.deepcopy(a)
    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            each_sum=a2[r][c]
            sum_count=1
            if in_range(r-1,c):
                each_sum+=a2[r-1][c] #up
                sum_count+=1
            if in_range(r,c+1):
                each_sum+=a2[r][c+1] #
                sum_count+=1
            if in_range(r+1,c):
                each_sum+=a2[r+1][c] #down
                sum_count+=1
            if in_range(r,c-1) :
                each_sum+=a2[r][c-1] #left
                sum_count+=1
            a[r][c] = each_sum//sum_count


for r1,c1,r2,c2 in winds:
    wind_movd(r1-1,c1-1,r2-1,c2-1)
    change_avg(r1-1,c1-1,r2-1,c2-1)

for row in a:
    print(*row)