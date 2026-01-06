from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def solution(edges):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    graph = defaultdict(list)
    nodes = set()
    for a,b in edges:
        graph[a].append(b)
        outdegree[a] += 1
        indegree[b] += 1
        nodes.add(a)
        nodes.add(b)
    for node in nodes:
        if outdegree[node] >= 2 and indegree[node]==0:
            start = node
    donut, stick, eight = 0,0,0
    
    for s in graph[start]:
        cur = s
        visited = set()
        while True:
            if cur in visited:
                donut += 1
                break
            visited.add(cur)
            
            d = outdegree.get(cur,0)
            if d == 0:
                stick += 1
                break
            if d >= 2:
                eight += 1
                break
                
            cur = graph[cur][0]
    answer = [start, donut, stick, eight]
    return answer