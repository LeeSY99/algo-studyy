n = int(input())
jump = list(map(int, input().split()))
import sys
ans = sys.maxsize

def backtrack(count,index):
    global ans
    if index == n-1:
        ans = min(ans, count)
        return
    elif index > n-1:
        return
    if jump[index] == 0:
        print(-1)
        quit()
    

    for i in range(1, jump[index]+1):
        backtrack(count+1,index+i)

backtrack(0,0)
print(ans)
