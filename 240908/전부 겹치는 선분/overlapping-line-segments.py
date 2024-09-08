n=int(input())

# points=[list(map(int, input().split())) for _ in range(n)]
#내가 푼 완전탐색으로
# for i in range(1,101):
#     can=1
#     for j in range(n):
#         if i<points[j][0]:
#             can=0
#             break
#         if i>points[j][1]:
#             can=0
#             break
#     if can:
#         print('Yes')
#         exit()

# print('No')
import sys

INT_MAX = sys.maxsize

n = int(input())

max_x1 = 0
min_x2 = INT_MAX

for _ in range(n):
    x1,x2=tuple(map(int,input().split()))
    max_x1=max(max_x1,x1)
    min_x2=min(min_x2,x2)

if min_x2>= max_x1: #x2(선의 오른쪽 끝)의 최솟값이 x1(선의 왼쪽 끝)의 최소값보다 크면 다 겹친다
    print('Yes')
else:
    print('No')