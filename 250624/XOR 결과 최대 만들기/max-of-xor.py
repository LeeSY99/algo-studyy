n, m = map(int, input().split())
nums = list(map(int, input().split()))

choosed = []

def choose(index, count):
    if index == n:
        if count == m:
            calc()
        return

    choosed.append(nums[index])
    choose(index+1, count+1)
    choosed.pop()

    choose(index+1, count)

ans = 0
def calc():
    global ans
    xor_result = 0
    for num in choosed:
        xor_result = xor_result ^ num
    ans = max(ans, xor_result)

choose(0,0)
print(ans)