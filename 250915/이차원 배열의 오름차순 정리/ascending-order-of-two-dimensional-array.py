n = int(input())
k = int(input())

left, right = 1, n*n
ans = n*n

while left <= right:
    mid = (left + right) // 2
    # i번째 행에 있는 숫자 중 M보다 같거나 작은 숫자의 개수 M/i개
    # p * i <= M -> p는 행 번호
    # mid를 값으로 잡아서 계산
    val = 0
    for i in range(1,n+1):
        val += min(n, mid//i)

    if val >= k:
        right= mid -1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)

    
