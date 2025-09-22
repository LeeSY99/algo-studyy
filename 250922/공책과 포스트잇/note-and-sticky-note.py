''' 
n개의 공책
공책의 번호는 포스트잇에 적힘
처음 i번의 번호가 다른 포스트잇에 적힌 횟수를 c_i
c_i가 h이상인 공책들이 h개 이상있는 경우 h-index
'''
n,k,l = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

def check(h):
    cnt = 0
    for i in range(n-h, n):
        if c[i] < h:
            cnt += h - c[i]

    return cnt <= k * l and c[n - h] + k >= h



left = 1
right = n
ans = 0


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)

