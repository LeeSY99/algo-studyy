n, m = map(int, input().split())
nums = [
    [[x] for x in map(int, input().split())] 
    for _ in range(n)
    ]
a = list(map(int, input().split()))

dr,dc = [0,1,1,1,0,-1,-1,-1,],[1,1,0,-1,-1,-1,0,1]
def in_range(r,c):
    return 0<=r<n and 0<=c<n


for num in a:
    temp = []
    ok = False
    for i in range(n):
        for j in range(n):
            k=0
            for _ in range(len(nums[i][j])-1,-1,-1):
                k += 1
                if nums[i][j][_] == num:
                    for m in range(k):
                        now_value = nums[i][j].pop()
                        max_num = 0
                        maxr, maxc = 0,0
                        for d in range(8):
                            nr = i + dr[d]
                            nc = j + dc[d]

                            if not in_range(nr,nc):
                                continue

                            if nums[nr][nc] and nums[nr][nc][0] > max_num:
                                maxr, maxc = nr, nc
                                max_num = nums[nr][nc][0]
                        if max_num == 0:
                            nums[i][j].append(now_value)
                            continue
                        temp.append(now_value)
                        if now_value == num:
                            while temp:
                                nums[maxr][maxc].append(temp.pop())
                            ok = True
                            break
                if ok:
                    break
            if ok:
                break
        if ok:
            break

                


for i in range(n):
    for j in range(n):
        if not nums[i][j]:
            print('None')
        else:
            while nums[i][j]:
                print(nums[i][j].pop(), end= ' ')
            print()


