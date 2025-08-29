from sortedcontainers import SortedSet

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
s_num = SortedSet()
s_len = SortedSet()

s_num.add(-1)
s_num.add(n+1)

# 길이, 시작 숫자, 끝 숫자 
s_len.add((-(n + 1), -1, n + 1))
d = []
for y in arr:
    s_num.add(y)

    z = s_num[s_num.bisect_right(y)]
    x = s_num[s_num.bisect_left(y) - 1]

    s_len.remove((-(z - x - 1), x, z )) #(x~z 구간 사라짐)
    s_len.add((-(y-x-1), x, y))
    s_len.add((-(z-y-1), y, z)) # x~y, y~z구간 새로 생겨남
    
    best_len = s_len[0][0]
    print(-best_len)