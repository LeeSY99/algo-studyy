n,m,k = map(int, input().split())
turn = list(map(int, input().split()))
score = [1 for _ in range(k)]

ans = 0
def backtrack(count):
    global ans
    ans = max(ans, check())
    if count == n:
        return


    for i in range(k):
        if score[i] >= m:
            continue
        
        score[i] += turn[count]
        backtrack(count+1)
        score[i] -= turn[count]
        

def check():
    val = 0
    for s in score:
        if s>=m:
            val +=1
    return val

backtrack(0)
print(ans)