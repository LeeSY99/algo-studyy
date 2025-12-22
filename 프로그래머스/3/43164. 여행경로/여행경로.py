from collections import defaultdict
import heapq
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for a,b, in tickets:
        graph[a].append(b)
        
    for a in graph:
        graph[a].sort(reverse=True)
        
    stack = ['ICN']
    
    while stack:
        cur = stack[-1]
        if graph[cur]:
            stack.append(graph[cur].pop())
        else:
            answer.append(stack.pop())
    
    
    return answer[::-1]