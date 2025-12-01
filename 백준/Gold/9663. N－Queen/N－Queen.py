import sys
n = int(sys.stdin.readline())
col = set()
cross_right = set()
cross_left = set()
ans = 0

def find(r):
    global ans
    if r == n:
        ans += 1
        return
    for c in range(n):
        if is_valid(r,c):
            col.add(c)
            cross_left.add(r+c)
            cross_right.add(r-c)

            find(r+1)

            col.remove(c)
            cross_left.remove(r+c)
            cross_right.remove(r-c)

def is_valid(r,c):
    if c in col:
        return False
    if r+c in cross_left:
        return False
    if r-c in cross_right:
        return False
    return True

find(0)
print(ans)




