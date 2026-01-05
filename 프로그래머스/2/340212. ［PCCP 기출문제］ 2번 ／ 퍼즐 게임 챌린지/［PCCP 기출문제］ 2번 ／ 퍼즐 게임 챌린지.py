def solution(diffs, times, limit):
    answer =  float('inf')
    l = 1
    r = 100000
    n = len(diffs)
    def solve(level):
        now = 0
        for i in range(n):
            diff = diffs[i]
            time_cur = times[i]
            if diff <= level:
                now += time_cur
            else:
                wrong = diff-level
                time_prev = times[i-1]
                now += (time_prev + time_cur) * wrong
                now += time_cur
        return now <= limit
            
    while l<=r:
        mid = (l+r)//2
        if solve(mid):
            answer = min(answer, mid)
            r = mid - 1
        else:
            l = mid + 1
        
    return answer