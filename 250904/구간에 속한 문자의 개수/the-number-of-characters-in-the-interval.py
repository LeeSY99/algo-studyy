MAX_C = 3

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
arr = [
    [0] * (m + 1)
    for _ in range(n + 1)
]
prefix_sum = [
    [
        [0] * (m + 1)
        for _ in range(n + 1)
    ]
    for _ in range(MAX_C + 1)
]


# 특정 숫자 c에 대해 
# (x1, y1), (x2, y2) 직사각형 구간 내의 원소의 합을 반환합니다.
def get_sum(c, x1, y1, x2, y2):
    return prefix_sum[c][x2][y2]     - prefix_sum[c][x1 - 1][y2] - \
           prefix_sum[c][x2][y1 - 1] + prefix_sum[c][x1 - 1][y1 - 1]


for i in range(1, n + 1):
    row = input()
    for j in range(1, m + 1):
        # 편의를 위해 
        # 입력받은 문자 a, b, c를 각각 
        # 1, 2, 3으로 바꿔서 저장해줍니다.
        if row[j - 1] == 'a':
            arr[i][j] = 1
        elif row[j - 1] == 'b':
            arr[i][j] = 2
        else:
            arr[i][j] = 3

# 누적합 배열을 만들어줍니다.
# prefix_sum[c][i][j] : 숫자가 c인 경우에 대한 누적합을 저장합니다.
for c in range(1, 4):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            additional_value = 0

            # (i, j) 위치에 적혀있는 숫자가 c인 경우에만
            # 값을 1 증가시켜줍니다.
            if arr[i][j] == c:
                additional_value = 1

            prefix_sum[c][i][j] = prefix_sum[c][i - 1][j] + \
                            prefix_sum[c][i][j - 1] - \
                            prefix_sum[c][i - 1][j - 1] + \
                            additional_value

# k개의 질의에 대한
# 답을 출력합니다.
for _ in range(k):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    print(get_sum(1, x1, y1, x2, y2),
          get_sum(2, x1, y1, x2, y2),
          get_sum(3, x1, y1, x2, y2))
