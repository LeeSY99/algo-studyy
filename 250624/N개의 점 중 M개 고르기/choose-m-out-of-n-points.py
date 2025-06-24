n, m = map(int, input().split())

points = []

for _ in range(n):
    a, b = map(int, input().split())
    points.append((a,b))

selected_points= []

def choose(index, count):
    if index == n:
        if count == m:
            calc()
        return

    selected_points.append(points[index])
    choose(index+1, count+1)
    selected_points.pop()

    choose(index+1, count)

import sys
ans = sys.maxsize
def calc():
    global ans
    max_distance = 0
    for i in range(m):
        for j in range(i+1, m):
            ai, aj = selected_points[i]
            bi, bj = selected_points[j]
            now_distance = (ai-bi)**2 + (aj-bj)**2
            max_distance = max(max_distance, now_distance)
    ans = min(ans, max_distance)

choose(0,0)
print(ans)

