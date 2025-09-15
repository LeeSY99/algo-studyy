m = int(input())
a, b = map(int, input().split())

''' 컴퓨터: 1~M 수 선택
이진탐색, 맞추면 벌칙
항상 가운데 값을 고름'''

min_ans = 100001
max_ans = 0

def play(x):
    left = 1
    right = m
    turn = 0
    while left<=right:
        turn +=1
        mid = (left + right) // 2
        if mid == x:
            return turn
        if mid < x:
            left = mid + 1
        if mid > x:
            right = mid - 1


for num in range(a, b+1):
    turn = play(num)
    min_ans = min(min_ans, turn)
    max_ans = max(max_ans, turn)

print(min_ans, max_ans)


