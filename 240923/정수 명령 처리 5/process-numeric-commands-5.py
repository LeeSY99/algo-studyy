n=int(input())
arr=[]

for _ in range(n):
    direction=input().split()
    if direction[0]=='push_back':
        arr.append(int(direction[1]))
    elif direction[0]=='pop_back':
        arr.pop()
    elif direction[0]=='size':
        print(len(arr))
    elif direction[0]=='get':
        print(arr[int(direction[1])-1])