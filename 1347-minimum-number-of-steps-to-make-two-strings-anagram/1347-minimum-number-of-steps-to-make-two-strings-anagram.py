class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        map_s = {}
        map_t = {}

        for c in s:
            map_s[c] = map_s.get(c,0) + 1
        
        for c in t:
            map_t[c] = map_t.get(c,0) + 1

        answer = 0
        for c, cnt in map_t.items():
            if c not in map_s:
                answer += cnt
            elif cnt > map_s[c]:
                answer += abs(cnt - map_s[c])
        return answer

        