class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for x in s:
            if x - 1 not in s:      # 연속 구간의 시작점
                cur = x
                length = 1
                while cur + 1 in s:
                    cur += 1
                    length += 1
                ans = max(ans, length)
        return ans
        