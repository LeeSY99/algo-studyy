n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
a = list(map(int, input().split()))

dr,dc = [0,1,1,1,0,-1,-1,-1,],[1,1,0,-1,-1,-1,0,1]
def in_range(r,c):
    return 0<=r<n and 0<=c<n

for num in a:
    for i in range(n):
        for j in range(n):
            if nums[i][j] == num:
                max_num = 0
                for r, c in zip(dr,dc):
                    nr, nc = i+nr, j+nc
                    if in_range(nr,nc):
                        if nums[nr][nc][0] > max_num:
                            maxr, maxc = nr,nc
                            max_num = nums[nr][nc]
                if max_num != 0:
                    while nums[i][j]:
                        nums[maxr][maxc].append(nums[i][j].pop())

for i in range(n):
    for j in range(n):
        print(*nums[i][j])


