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

def drop_ball(root,k):
    x = root

    while True:
        sub_ball[x] += 1
        l, r = left[x], right[x]
        ## 자식 0개
        if l == -1 and r == -1:
            ball[x] += 1
            return x
        ## 자식 1개
        if l == -1:
            x = r
            continue
        if r == -1:
            x = l
            continue
        ## 자식 2개
        if k%2 == 1:
            x = l
            k = (k+1)//2
        else:
            x = r
            k = k//2
        
    


last_pos = drop_ball(1, k)
print(last_pos)

