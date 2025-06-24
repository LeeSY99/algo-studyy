n = int(input())
a = list(map(int, input().split()))

choosed_num = []
def choose(index, count):
    if index == 2*n:
        if count == n:
            calc()
        return

    choosed_num.append(a[index])
    choose(index+1, count+1)
    choosed_num.pop()

    choose(index+1, count)

import sys
ans = sys.maxsize

def calc():
    global ans
    part1 = []
    part2 = []
    i = 0
    for num in a:
        if i<n and num == choosed_num[i]:
            part1.append(num)
            i+=1
        else:
            part2.append(num)

    ans = min(ans, abs(sum(part1) - sum(part2)))

choose(0,0)
print(ans)

