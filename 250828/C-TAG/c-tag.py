''' a t g c m개의 알파벳 종이 2n장
'''
n,m = map(int, input().split())
g1 = [list(input()) for _ in range(n)]
g2 = [list(input()) for _ in range(n)]

count = 0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            s1 = set()
            for l in range(n):
                w1 = g1[l][i] + g1[l][j] + g1[l][k]
                s1.add(w1)
            
            flag = True
            for l in range(n):
                w2 = g2[l][i] + g2[l][j] + g2[l][k]
                if w2 in s1:
                    flag = False
                    break
            
            if flag:
                count+=1

print(count)



