n = int(input())
nums1 = list(map(int, input().split()))

m = int(input())
nums2 = list(map(int, input().split()))

s1 = set(nums1)

for num in nums2:
    if num in s1:
        print(1)
    else:
        print(0)