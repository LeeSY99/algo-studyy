'''n*m격자 집의 높이 1~100
비가 k만큼 오면 높이가 k 이하인 집은 잠김
잠기지 않은 집끼리 인접해 있으면 같은 안전영역으로 보고
안전영역을 구함 -> 안전영역이 최대일때의 K와 그때의 안전영역 수'''
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
def in_range(r,c):
    return 0<=r<n and 0<=c<m


def dfs(r,c):
    visited[r][c] = 1
    for dr, dc in zip(drs,dcs):
        nr, nc = r+dr, c+dc
        if in_range(nr, nc) and not visited[nr][nc] and house[nr][nc] > k:
            dfs(nr,nc)

def calc_safe_area():
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and house[i][j] > k:
                count+=1
                dfs(i,j)
    return count



max_safe_area = 0
ans_k = 1
for k in range(1, 100):
    visited = [[0]*m for _ in range(n)]
    safe_area = calc_safe_area()
    if safe_area > max_safe_area:
        max_safe_area = safe_area
        ans_k = k

print(ans_k, max_safe_area)