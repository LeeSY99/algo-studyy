class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(baseCosts)
        m = len(toppingCosts)

        def dfs(index, cost):
            nonlocal min_interval, answer
            if index == m:
                if abs(cost-target) < min_interval:
                    min_interval = abs(cost-target)
                    answer = cost
                elif abs(cost-target) == min_interval and answer > cost:
                    answer = cost 
                return

            dfs(index+1, cost)
            dfs(index+1, cost + toppingCosts[index])
            dfs(index+1, cost + 2*toppingCosts[index])

        min_interval = float('inf')
        answer = 0
        for base in baseCosts:
            dfs(0, base)
            

        return answer