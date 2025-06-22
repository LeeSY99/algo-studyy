k, n = map(int, input().split())


nums = []

def backtrack(count):
    global nums
    if count == n:
        print_num()
        return

    for i in range(1,k+1):
        if count>=2 and nums[-1] == i and nums[-2] == i:
            continue
        nums.append(i)
        backtrack(count+1)
        nums.pop()

def print_num():
    print(*nums)

backtrack(0)