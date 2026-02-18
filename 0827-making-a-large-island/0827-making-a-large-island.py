class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        drs,dcs = [0,1,0,-1],[1,0,-1,0]

        size_map = {}
        index = 2
        answer = 0

        def in_range(r,c):
            return 0<=r<n and 0<=c<n

        def dfs(r,c,idx):
            if not in_range(r,c) or grid[r][c] != 1:
                return 0
            grid[r][c] = idx
            cnt = 1
            cnt += dfs(r,c+1,idx)
            cnt += dfs(r+1,c,idx)
            cnt += dfs(r,c-1,idx)
            cnt += dfs(r-1,c,idx)
            return cnt

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i,j,index)
                    size_map[index] = size
                    answer = max(answer, size)
                    index +=1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cur = 1
                    visited = set()
                    for dr, dc in zip(drs,dcs):
                        nr, nc = i+dr, j+dc
                        if not in_range(nr,nc):
                            continue
                        if grid[nr][nc] == 0:
                            continue
                        if grid[nr][nc] in visited:
                            continue

                        visited.add(grid[nr][nc]) 
                        cur += size_map[grid[nr][nc]]
                    answer = max(answer, cur)
        return answer

        

        