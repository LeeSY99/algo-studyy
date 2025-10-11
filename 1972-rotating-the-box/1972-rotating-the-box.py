class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n,m = len(boxGrid), len(boxGrid[0])
        newgrid = [[None]*n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                newgrid[j][n-1-i] = boxGrid[i][j]

        n,m = len(newgrid), len(newgrid[0])
        for j in range(m):
            write = n-1
            i = n-1
            while i >= 0:
                if newgrid[i][j] == '*':
                    write = i-1
                    i -= 1
                else:
                    ##돌이 낙하할 구간을 구함
                    seg_bottom = i
                    while i>=0 and newgrid[i][j] != '*':
                        i -= 1
                    seg_top = i+1

                    ##구간 내 돌 개수 구함
                    stones = 0
                    for ii in range(seg_top, seg_bottom + 1):
                        if newgrid[ii][j] == '#':
                            stones += 1
                    
                    ##돌 채우기
                    write = seg_bottom
                    for _ in range(stones):
                        newgrid[write][j] = '#'
                        write -= 1
                    ## 빠진 돌 빈칸 매꿈
                    for ii in range(write, seg_top-1, -1):
                        newgrid[ii][j] = '.'

        print(newgrid)
        return newgrid