class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        uf = {}
        l = {}
        for n in nums:
            uf[n] = n
            l[n] = 1
        
        def union(a,b):
            A = find(a)
            B = find(b)
            if A==B:
                return
            if A < B:
                A,B = B,A
            uf[A] = B
            l[B] += l[A]

        def find(x):
            if x == uf[x]:
                return x
            uf[x] = find(uf[x])
            return uf[x]

        for n in nums:
            if n-1 in nums:
                union(n,n-1)
            if n+1 in nums:
                union(n,n+1)
            
        for n in nums:
            if find(n) == n:
                ans = max(ans, l[n])
        return ans
        