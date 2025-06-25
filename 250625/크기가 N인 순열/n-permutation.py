n = int(input())

visited = [0] *(n+1)
nums = []

def backtrack(count):
    if count == n:
        print_ans()
        return
    
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        
        visited[i]=1
        nums.append(i)
        backtrack(count+1)

        visited[i] = 0
        nums.pop()

def print_ans():
    for num in nums:
        print(num, end = ' ')
    print()

backtrack(0)