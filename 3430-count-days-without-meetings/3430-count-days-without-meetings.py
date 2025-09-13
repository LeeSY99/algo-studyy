class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        points = []
        for x, y  in meetings:
            points.append((x,1))
            points.append((y,-1))
        
        points.sort(key = lambda x: (x[0], -x[1]))
        ans = days
        segs = 0
        # print(points)
        for x, v in points:
            if segs == 0:
                start = x
            
            segs += v

            if segs == 0:
                ans -= (x - start + 1)
        
        return ans
            

        