class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) < 2:
            return True
        if stones[1] != 1:
            return False

        stones_set = set(stones)
        dp = defaultdict(set)
        dp[0].add(0)
        last = stones[-1]

        for stone in stones:
            for last_jump in dp[stone]:
                for next_jump in (last_jump-1, last_jump, last_jump+1):
                    if next_jump <= 0:
                        continue
                    next_stone = stone + next_jump
                    if next_stone == last:
                        return True
                    if next_stone in stones_set:
                        dp[next_stone].add(next_jump)
        return False





        
        
            

        