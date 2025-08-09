n,m = map(int, input().split())

treasure = []
for _ in range(n):
    w,v = map(int, input().split())
    treasure.append((w,v))

treasure.sort(key = lambda x: -(x[1]/x[0]))


ans = 0
for w, v in treasure:
    if m//w >= 1:
        ans += v
        m -= w
    else:
        ans += m/w*v
        break
    
#     print(ans, m)
# print('----')
# print(treasure)
print(f'{ans:.3f}')
