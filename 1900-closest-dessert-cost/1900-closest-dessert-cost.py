class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = float('inf')
        now_diff = float('inf')
        
        def backtrack(value, idx, target):
            nonlocal ans, now_diff
            if (abs(value - target), value) < (now_diff, ans):
                ans = value
                now_diff = abs(value - target)
            
            
            if idx == len(toppingCosts):
                return

            
            backtrack(value, idx+1, target)
            backtrack(value + toppingCosts[idx], idx + 1, target)
            backtrack(value + 2*toppingCosts[idx], idx + 1, target)

        for basecost in baseCosts:
            backtrack(basecost, 0, target)
        return ans
