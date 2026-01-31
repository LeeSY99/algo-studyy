class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = defaultdict(set)
        #dp[i][j] i -> j점프 가능할 경우 점프 거리

        
        dp[0].add(0)

        for i in range(n):
            stone = stones[i]
            for last_jump in dp[stone]:
                for next_jump in [last_jump - 1, last_jump, last_jump + 1]:
                    if next_jump <= 0:
                        continue
                    next_stone = stone + next_jump
                    if next_stone in stones:
                        dp[next_stone].add(next_jump)
        
        last = stones[-1]
        print(dp)
        return len(dp[last]) > 0





        
        
            

        