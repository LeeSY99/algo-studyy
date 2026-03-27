class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        

        count = 0
        points = []
        
        for s, e in meetings:
            points.append((s,1))
            points.append((e+1,-1))

        points.sort()

        start = 0
        answer = 0
        print(points)
        for x, v in points:
            if count == 0:
                print(x,v,count) 
                answer += x-start-1
            count += v
            if count == 0:
                start = x-1
        
        answer += days-start

        return answer


        