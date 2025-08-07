n = int(input())

left = 0
right = 10**10 


def check(num):
    return num - num//3 - num//5 + num//15

ans = 10**10
while left<=right:
    mid = (left + right) // 2
    if check(mid) >= n:
        ans = min(ans, mid)
        right = mid-1
    else:
        left = mid+1
    
print(ans)
    