class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hashmap = {}
        hashset = set()
        answer = 0
        n = len(hours)
        for i in range(n):
            hour = hours[i]
            hour = hour % 24
            remain = (24 - hour)%24
            answer += hashmap.get(hour, 0)
            hashmap[remain] = hashmap.get(remain,0) + 1

        return answer

        
