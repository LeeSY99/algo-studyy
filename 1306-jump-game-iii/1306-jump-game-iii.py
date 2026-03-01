class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = [False] * n
        visited[start] = True
        if arr[start] == 0:
            return True

        q = deque([start])
        while q:
            now = q.popleft()
            if arr[now] == 0:
                return True
            jump = arr[now]

            if 0 <= now - jump < n and not visited[now-jump]:
                visited[now-jump] = True
                q.append(now-jump)
                # if arr[now-jump] == 0:
                #     return True
            if 0 <= now + jump < n and not visited[now+jump]:
                visited[now+jump] = True
                q.append(now+jump)
                # if arr[now+jump] == 0:
                #     return True
        return False

        
        