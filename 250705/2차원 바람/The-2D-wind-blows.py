'''n*m 행렬 q번 바람
바람 불면 범위 내 경계 숫자는 시계방향으로 한칸씩 시프트
그리고 범위 내 모든 숫자 상하좌우 인접한 값+해당 위치 값의 평균을 버림한 값(동시에)'''

n, m, q =map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]

def print_building():
    for b in building:
        print(*b)
    # print('---')
    
def flow(r1,c1,r2,c2):
    temp_top = building[r1][c2]
    temp_right = building[r2][c2]
    temp_bottom = building[r2][c1]
    temp_left = building[r1][c1]
    for c in range(c2,c1+1,-1):
        building[r1][c] = building[r1][c-1]
    building[r1][c1+1] = temp_left

    for r in range(r2,r1+1,-1):
        building[r][c2] = building[r-1][c2]
    building[r1+1][c2] = temp_top

    for c in range(c1,c2-1):
        building[r2][c] = building[r2][c+1]
    building[r2][c2-1] = temp_right

    for r in range(r1, r2-1):
        building[r][c1] = building[r+1][c1]
    building[r2-1][c1] = temp_bottom

def in_range(r,c):
    return 0<=r<n and 0<=c<m

def change(r1,c1,r2,c2):
    global building
    new_building = [arr[:] for arr in building]
    drs, dcs = [0,-1,1,0,0], [0,0,0,-1,1]
    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            count = 0
            value = 0
            for dr, dc in zip(drs, dcs):
                nr, nc= r+dr, c+dc
                if in_range(nr, nc):
                    count +=1
                    value += building[nr][nc]
            new_building[r][c] = value//count
    building = new_building


for _ in range(q):
    r1,c1, r2,c2 = map(int, input().split())
    flow(r1-1,c1-1,r2-1,c2-1)
    # print_building()
    change(r1-1,c1-1,r2-1,c2-1)
    # print_building()
print_building()


