a,b,c=map(int,input().split())

max_num=0

# for i in range(c):
#     for j in range(c):
#         num=a*i+b*j
#         if num<=c:
#             max_num=max(max_num,num)
#         else:
#             break

# print(max_num)

for i in range(c//a +1):
    num=a*i
    num_b=(c-num) //b
    num+=num_b * b
    max_num=max(max_num,num)

print(max_num)