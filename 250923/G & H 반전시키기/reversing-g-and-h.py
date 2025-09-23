n = int(input())

arr1 = list(input())
arr2 = list(input())

start = False
count = 0
for i in range(n):
    if not start and arr1[i] != arr2[i]:
        start = True
        count +=1
        
    if start and arr1[i] == arr2[i]:
        start = False

print(count)