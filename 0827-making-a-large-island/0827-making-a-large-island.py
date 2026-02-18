class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        drs, dcs = [0,1,0,-1],[1,0,-1,0]
        def in_range(r,c):
            return 0<=r<n and 0<=c<n

        def bfs(r,c,num):
            global ans
            q = deque([(r,c)])
            visited[r][c] = True
            points = [(r,c)]
            count = 1
            while q:
                r,c = q.popleft()
                for dr,dc in zip(drs,dcs):
                    nr,nc = r+dr, c+dc
                    if in_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr,nc))
                        count += 1
                        points.append((nr,nc))
            
            for r,c in points:
                island[r][c] = (count, num)
            return count


        island = [[(0,0)] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        ans = 0
        num = 1
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    ans = max(ans, bfs(i,j,num))
                    num += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    isl = 1
                    is_no = []
                    for dr, dc in zip(drs,dcs):
                        nr,nc = r+dr, c+dc
                        if in_range(nr,nc):
                            count, num = island[nr][nc]
                            if num in is_no:
                                continue
                            isl += count
                            is_no.append(num)
                    print(isl)
                    ans = max(ans, isl)

        return ans
        

        