import sys
arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

def in_range(r,c):
    return 0<=r and r<19 and 0<=c and c<19

drs,dcs=[1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

for i in range(19):
    for j in range(19):
        if arr[i][j] ==0:
            continue

        for dr,dc in zip(drs,dcs):
            curt=1
            curr=i
            curc=j
            while 1:
                nr=curr+dr
                nc=curc+dc
                if in_range(nr,nc)==False:
                    break
                if arr[nr][nc] != arr[i][j]:
                    break
                curt+=1
                curr=nr
                curc=nc
            
            if curt==5:
                print(arr[i][j])
                print(i+2*dr+1, j+2*dc+1)
                sys.exit()
print(0)