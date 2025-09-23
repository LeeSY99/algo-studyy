n = int(input())

arr = []
for _ in range(n):
    x,y = map(int, input().split())
    arr.append((y, x))

arr.sort()
left = 0
right = n-1
ans = 0


while left <= right:
    ly, lx = arr[left]
    ry, rx = arr[right]

    ans = max(ans, ly+ry)

    if lx < rx:
        arr[right] = (ry, rx-lx)
        left += 1

    elif lx > rx:
        arr[left] = (ly, lx-rx)
        right -=1
    
    else:
        left+=1
        right-=1

print(ans)
