n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

nums = {}

count = 0
for i in range(n):
    for j in range(n):
        s = A[i] + B[j]
        if -s in nums:
            count += nums[-s]
    
        if s in nums:
            nums[s] += 1
        else:
            nums[s] = 1

for i in range(n):
    for j in range(n):
        s = C[i] + D[j]
        if -s in nums:
            count += nums[-s]
    
        if s in nums:
            nums[s] += 1
        else:
            nums[s] = 1

print(count//2)
        
