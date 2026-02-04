R,C,M = map(int, input().split())

grid = [[[] for _ in range(C)] for _ in range(R)]
# print(grid)
drs,dcs = [-1,1,0,0],[0,0,1,-1]
sharks = {}

class Shark:
    def __init__(self, r,c,s,d,z):
        self.r = r
        self.c = c
        self.speed = s
        self.dir = d-1
        self.size = z
        self.is_alive = True

    def move(self):
        if self.dir in (0,1):
            dist = 2 * (R - 1)
            move_dist = self.speed % dist
            p = self.r if self.dir == 1 else dist - self.r
            p = (p+move_dist) % dist

            self.r = p if p <= R-1 else dist - p
            self.dir = 1 if p < R-1 else 0
        else:
            dist = 2 * (C-1)
            move_dist = self.speed % dist
            p = self.c if self.dir == 2 else dist - self.c
            p = (p+move_dist) % dist
            self.c = p if p <= C-1 else dist-p
            self.dir = 2 if p < C-1 else 3

    def __repr__(self):
        return f'{self.size}, {self.dir}'

def eat():
    for r in range(R):
        for c in range(C):
            if len(grid[r][c]) >= 2:
                max_size = 0
                for shark in grid[r][c]:
                    if shark.size > max_size:
                        max_size = shark.size
                        remain_shark = shark
                for shark in grid[r][c]:
                    if shark.size < max_size:
                        shark.is_alive = False
                grid[r][c] = [remain_shark]




ans = 0
for i in range(M):
    r,c,s,d,z = map(int, input().split())
    r-=1
    c-=1
    new_shark = Shark(r,c,s,d,z)
    grid[r][c].append(new_shark)
    sharks[i] = new_shark

for c in range(C):
    # for g in grid:
    #     print(*g)
    for r in range(R):
        if grid[r][c]:
            shark = grid[r][c][0]
            if shark.is_alive:
                ans += shark.size
                shark.is_alive = False
                break
    #shark move
    grid = [[[] for _ in range(C)] for _ in range(R)]
    for idx, shark in sharks.items():
        if shark.is_alive:
            shark.move()
            r = shark.r
            c = shark.c
            grid[r][c].append(shark)

    #shark eat
    eat()
    # print(ans)

print(ans)

