''' 도시 n개, 간선 m 개
도시 번호 : 0 ~ n-1, 방향x
두 도시 연결하는 간선 여러개 가능, 자기자신연결 

출발: 0번도시

1) 랜드 건설
    n,m
    (v,u,w) : v -> u 도시 잇고 가중치 w

2) 여행상품 생성
    (id, revenue, dest) 상품 만들고
    revenue: 매출
    dest: 도착지

3) 취소
    id 를 가진 여생상품 삭제

4) 최적의 여행 상품 판매
    관리 목록에서 조건에 맞는 여행상품 판매
    조건
        revenue-cost 가 최대 - cost: (출발-> 도착지까지 최단거리)
        id 작음
    도착지에 도달할 수 없거나 cost가 revenue보다 더 크면 판매불가

    판매후 id 출력, 목록에서 제거
    판매가능한게 없다면 -1 출력

5) 출발지 변경
    출발지를 전부 s로 변경

'''
import heapq, sys

q = int(input())
graph = [[]]
packages = []
dist = []
def build_land(remain):
    global graph, dist
    info = remain[2:]
    graph = [[] for _ in range(n)]

    for i in range(n):
        index = 3*i
        v, u, w = info[index], info[index+1], info[index+2]
        graph[v].append((u,w))
        graph[u].append((v,w))
    dist = dijkstra(0)

def dijkstra(start):
    global dist
    dist = [sys.maxsize] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        now_dist, now_land = heapq.heappop(q)

        if now_dist > dist[now_land]:
            continue

        for v, weight in graph[now_land]:
            next_dist = dist[now_land] + weight
            if next_dist < dist[v]:
                dist[v] = next_dist
                heapq.heappush(q,(next_dist, v))
    
    return dist

class Travel_package:
    def __init__(self, id, revenue, dest):
        self.id = id
        self.start = 0
        self.revenue = revenue
        self.dest = dest
        self.cost = dist[self.dest]
    
    

    def __lt__(self, other):
        if self.revenue - self.cost != other.revenue - other.cost:
            return -(self.revenue - self.cost) < -(other.revenue - other.cost)
        if self.id != other.id:
            return self.id < other.id 

    def change(self):
        self.cost = self.cost = dist[self.dest]
    
def make_package(remain):
    id, revenue, dest = remain[0], remain[1], remain[2]
    package = Travel_package(id, revenue, dest)
    heapq.heappush(packages, package)
    #########
    

def cancel_package(remain):
    global packages
    target_id = remain[0]
    new_heap = [pkg for pkg in packages if pkg.id != target_id]
    heapq.heapify(new_heap)
    packages = new_heap

def sell_best_package():
    
    if not packages:
        print(-1)
        return
    
    for package in packages:
        if package.revenue - package.cost >=0:
            print(package.id)
            packages.remove(package)
            heapq.heapify(packages)
            return
    print(-1)
    return

def change_start(remain):
    global dist
    s = remain[0]
    dist = dijkstra(s)
    for package in packages:
        package.start = s
        package.change()
    


for _ in range(q):
    direction, *remain = map(int, input().split())
    if direction == 100:
        n, m = remain[0], remain[1]
        build_land(remain)
    elif direction == 200:
        make_package(remain)
    elif direction == 300:
        cancel_package(remain)
    elif direction == 400:
        sell_best_package()
    elif direction == 500:
        # print(500)
        change_start(remain)

    # print(f'{_+1}turn')
    # for package in packages:
    #     print(package.id, package.revenue, package.cost)
    # print('--------------------------')