''' n*n 공간
한변의 길이 n 2차원 평면
그 사이 길이 m인 정육면체 벽

1) 미지의 공간의 평면도 - 위에서 내려다본 맵 3-시간의 벽, 4- 탈출구
2) 시간의 벽의 단면도 - 벽의 윗면, 동서남북 단면도

타임머신 - 벽 윗면 어딘가 위치 (2)
벽에서 바닥으로 이어지는 출구는 하나

바닥에는 f개의 이상현상
    (r,c)에서 시작하여 매 v_i의 배수 턴마다 방향 d_i로 한칸씩 확산, 확산돼도 기존 이상현상은 남아있음
    장애물과 탈출구가 없는 빈 공간으로만 확산 (동서남북) 순

매 턴마다 상하좌우 이동 -> 장애물과 이상현상을 피해 탈출구에 도달해야함

탈출구까지 이동하는 최소시간 출력, 탈출 불가능 시 -1

3차원 따로 2차원 따로
-------
시간에 따라 제약이 달라지는 bfs
visited - true/false 대신 시간으로 기록
-> 여기서 이상현상 시간과 비교해 지나갈 수 있는지 판단
--------
3차원 겉면 bfs -> 2가지 방식 가능
1) 격자를 그래프로 변환 (기본적인 방식)
2) 기본 bfs로 하다가 네 변과 맞닿아 있는 경우 다른 면으로 transition 따져줌
'''
DEBUG = False
from collections import deque
#####input######
N,M,F = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
## 동, 서, 남, 북, 윗
EAST, WEST, SOUTH, NORTH, TOP = 0,1,2,3,4
views = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
strange = [tuple( map(int, input().split())) for _ in range(F)]

drs, dcs = [0,0,1,-1],[1,-1,0,0]
##################

def cube_escape():
    #출발, 
    for i in range(M):
        for j in range(M):
            if views[TOP][i][j] == 2:
                start_r, start_c = i,j
                break
    #탈출, 2차원의 시작점
    escape_2d_r, escape_2d_c = -1,-1
    #큐브 탈출 면, 좌표
    escape_3d_face, escape_3d_r, escape_3d_c = -1,-1, -1
    #2D에서 큐브 좌상단 좌표 찾기 3
    cube_start_r, cube_start_c = -1,-1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 3:
                cube_start_r, cube_start_c = i,j
                break
        if cube_start_r != -1:
            break
    #2D에서 큐브 좌상단 좌표 기준 4방향 탐색해서 큐브 출구 찾기
    if cube_start_r -1 >= 0:
        for c in range(cube_start_c,cube_start_c+M):
            if grid[cube_start_r-1][c] == 0:
                escape_2d_r, escape_2d_c = cube_start_r-1, c 
                escape_3d_face, escape_3d_r, escape_3d_c = NORTH, M-1, M -1 -(c-cube_start_c)
    if cube_start_r + M < N :
        for c in range(cube_start_c,cube_start_c+M):
            if grid[cube_start_r+M][c] == 0:
                escape_2d_r, escape_2d_c = cube_start_r+M, c 
                escape_3d_face, escape_3d_r, escape_3d_c = SOUTH, M-1, c-cube_start_c
    if cube_start_c -1 >= 0:
        for r in range(cube_start_r,cube_start_r+M):
            if grid[r][cube_start_c -1] == 0:
                escape_2d_r, escape_2d_c = r, cube_start_c -1
                escape_3d_face, escape_3d_r, escape_3d_c = WEST, M-1, r - cube_start_r
    if cube_start_c + M < N :
        for r in range(cube_start_r,cube_start_r+M):
            if grid[r][cube_start_c + M] == 0:
                escape_2d_r, escape_2d_c = r, cube_start_c + M
                escape_3d_face, escape_3d_r, escape_3d_c = EAST, M-1, M -1 - (r-cube_start_r)

    #bfs (면,r,c)
    q = deque([(TOP, start_r, start_c)])
    visited = [[[float('inf')] * M for _ in range(M)] for _ in range(5)]
    visited[TOP][start_r][start_c] = 0

    while q:
        face, r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            if 0 <= nr < M  and 0<= nc < M and views[face][nr][nc] == 0 and visited[face][nr][nc] > visited[face][r][c] + 1:
                q.append((face,nr,nc))
                visited[face][nr][nc] = visited[face][r][c] + 1

        #transition 다른 평면
        transition_candidates = []
        if face == TOP:
            if r == 0:
                transition_candidates.append((NORTH, 0, M-c-1))
            if r == M-1:
                transition_candidates.append((SOUTH, 0, c))
            if c == 0:
                transition_candidates.append((WEST, 0, r))
            if c == M-1:
                transition_candidates.append((EAST, 0, M-r-1))
        if face == WEST:
            if r == 0:
                transition_candidates.append((TOP, c, 0))
            if c == 0:
                transition_candidates.append((NORTH, r, M-1))
            if c == M-1:
                transition_candidates.append((SOUTH, r, 0))
        if face == EAST:
            if r == 0:
                transition_candidates.append((TOP, M-c-1, M-1))
            if c == 0:
                transition_candidates.append((SOUTH, r, M-1))
            if c == M-1:
                transition_candidates.append((NORTH, r, 0))
        if face == SOUTH:
            if r == 0:
                transition_candidates.append((TOP, M-1, c))
            if c == 0:
                transition_candidates.append((WEST, r, M-1))
            if c == M-1:
                transition_candidates.append((EAST, r, 0))
        if face == NORTH:
            if r == 0:
                transition_candidates.append((TOP, 0, M-1-c))
            if c == 0:
                transition_candidates.append((EAST, r, M-1))
            if c == M-1:
                transition_candidates.append((WEST, r, 0))

        for new_face, nr, nc in transition_candidates:
            if views[new_face][nr][nc] == 0 and visited[new_face][nr][nc] > visited[face][r][c] + 1:
                q.append((new_face,nr,nc))
                visited[new_face][nr][nc] = visited[face][r][c] + 1

    if visited[escape_3d_face][escape_3d_r][escape_3d_c] != float('inf'):
        #탈출가능
        return visited[escape_3d_face][escape_3d_r][escape_3d_c], escape_2d_r, escape_2d_c
    else:
        return -1, escape_2d_r, escape_2d_c

def escape_2d(start_time, st_r, st_c):
    if start_time == -1:
        return -1
    if DEBUG:
        print('출발좌표',st_r, st_c)
    #도착지점
    ed_r, ed_c = -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 4:
                ed_r, ed_c = i, j

    if DEBUG:
        print('2d 출구:', ed_r, ed_c)
    limit = [[float('inf')] * N for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]

    #이상현상 배열
    for r,c,d,v in strange:
        for t in range(N):
            nr, nc = r+ t*drs[d], c+ t*dcs[d]
            if 0<=nr<N and 0<=nc<N and grid[nr][nc] == 0:
                limit[nr][nc] = v * t
            else: break
    

    #2차원 bfs
    q = deque([(st_r, st_c)])
    visited[st_r][st_c] = start_time + 1
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr, nc = r+dr, c+dc
            # 범위, 빈공간, 시간제약, visited
            if 0<=nr<N and 0<=nc<N and grid[nr][nc] in [0,4] and visited[r][c] + 1 < limit[nr][nc] and visited[r][c]+1 < visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
    if DEBUG:
        for vi in visited:
            for v in vi:
                print(v, end = '  ')
            print()
    if visited[ed_r][ed_c] == float('inf'):
        return -1
    return visited[ed_r][ed_c]



escape_cube_time, st_2d_r, st_2d_c = cube_escape()
# print(escape_cube_time)
print(escape_2d(escape_cube_time, st_2d_r, st_2d_c))



