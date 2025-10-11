from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = map(int, time.split(':'))
            times[name].append(hour*60 + minute)

        ans = []
        for name, arr in times.items():
            arr.sort()
            for i in range(2,len(arr)):
                if arr[i] - arr[i-2] <= 60:
                    ans.append(name)
                    break
        
        return sorted(ans)

