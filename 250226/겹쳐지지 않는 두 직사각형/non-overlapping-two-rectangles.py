import sys

# 입력값 설정
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(i, j):
    return 0 <= i < n and 0 <= j < m

def rect_sum(x1, y1, x2, y2):
    total = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            total += grid[x][y]
    return total

def is_overlapping(r1, c1, r2, c2, r3, c3, r4, c4):
    if c2 < c3 or c1 > c4:  # 완전히 왼쪽 또는 오른쪽
        return False
    if r2 < r3 or r1 > r4:  # 완전히 위쪽 또는 아래쪽
        return False
    return True  # 위 조건이 아니면 겹침

def find_sec_rec(r1, c1, r2, c2):
    max_rec2 = -sys.maxsize
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not is_overlapping(r1, c1, r2, c2, i, j, k, l):
                        max_rec2 = max(max_rec2, rect_sum(r1, c1, r2, c2) + rect_sum(i, j, k, l))
    return max_rec2

def find_rec():
    max_rec1 = -sys.maxsize
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_rec1 = max(max_rec1, find_sec_rec(i, j, k, l))
    return max_rec1

# 결과 출력
result = find_rec()
print(result)
