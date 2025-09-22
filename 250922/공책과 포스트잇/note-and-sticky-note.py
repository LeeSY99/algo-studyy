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
    ##가장 큰 h개만 보면 됨
    for i in range(n-h, n):
        if c[i] < h:
            cnt += h - c[i]
        # 바꿔야 할 양의 총량이 k*l보다 작고
        # 개별적으로는 최대 k개밖에 증가시킬 수 없음 그래서 가장 작은 값을 골라 비교
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

