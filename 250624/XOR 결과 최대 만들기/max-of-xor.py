n, m = map(int, input().split())

choosed = []
def choose(cur_num, count):
    if cur_num == n+1:
        if count == m:
            calc()
        return

    choosed.append(cur_num)
    choose(cur_num+1, count+1)
    choosed.pop()

    choose(cur_num+1, count)

ans = 0
def calc():
    global ans
    xor_result = 0
    for num in choosed:
        xor_result = xor_result ^ num
    ans = max(ans, xor_result)

choose(1,0)
print(ans)