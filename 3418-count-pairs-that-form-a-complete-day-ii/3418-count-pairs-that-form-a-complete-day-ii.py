class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0
        times = {}

        for i in range(n):
            if (24 - hours[i]) % 24 in times:
                ans += times[(24 - hours[i]) % 24]
            if hours[i] % 24 in times:
                times[hours[i] % 24] +=1
            else:
                times[hours[i] % 24] = 1

        return ans
            

        