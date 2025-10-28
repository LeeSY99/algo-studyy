'''
1. 자식 노드가 1개 -> 해당 자식노드
2. 자식 노드가 2개
    왼쪽 -> 왼쪽 서브트리 공 개수가 오른쪽 서브트리보다 작거나 같음
    오른쪽 -> 이외의 경우
3. 자식노드 0개 -> 멈춤 '''
n = int(input())
left = [0] * (n+1)
right = [0] * (n+1)
ball = [0] * (n+1)
sub_ball = [0] * (n+1)

for i in range(1,n+1):
    l, r = map(int, input().split())
    left[i] = l
    right[i] = r

k = int(input())

def drop_ball(root):
    x = root
    path = []

    while True:
        path.append(x)
        l, r = left[x], right[x]

        if l == -1 and r == -1:
            ball[x] += 1
            break
        
        if l == -1:
            x = r
            continue
        if r == -1:
            x = l
            continue
        
        if sub_ball[l] <= sub_ball[r]:
            x = l
        else:
            x = r
    for u in path:
        sub_ball[u] += 1
    return x

last_pos = -1
for i in range(n):
    last_pos = drop_ball(1)
print(last_pos)

