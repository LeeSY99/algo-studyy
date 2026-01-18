class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = {}
        ans = 0

        for n in nums:
            if n not in num:
                lenth = 1
                left = n
                right = n

                if n-1 in num:
                    lenth += num[n-1]
                    left = n - num[n-1]
                if n+1 in num:
                    lenth += num[n+1]
                    right = n + num[n+1]

                num[n] = lenth
                num[left] = lenth
                num[right] = lenth
                ans = max(ans, lenth)
        return ans

        