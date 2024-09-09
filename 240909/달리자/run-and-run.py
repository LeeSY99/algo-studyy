n=int(input())

ai=list(map(int,input().split()))
bi=list(map(int,input().split()))

#그리디 알고리즘 현재 집에 더 많이 있다면 다음집으로 이동하는 방식으로 풀이
people=0
count=0
for i in range(n-1):
    if ai[i]>bi[i]:
        count += (ai[i]-bi[i])
        ai[i+1] += (ai[i]-bi[i])

print(count)