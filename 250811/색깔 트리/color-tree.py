''' 각 노드 색깔color, 최대 깊이max_depth속성을 가짐
노드 추가, 색 변경 처리

1) 노드 추가
     노드를 트리에 추가함
        m_id, p_id, color, max_depth
    -m_id - 고유번호
    -p_id = 부모노드 번호
    -color :  1~5 발주노초파 순
    -last_updated : 마지막 색 변경시각
    -p_id : -1이면 새 트리의 루트가 됨
    -max_depth : 서브트리의 최대 깊이
    -자식노드

    기존 노드들의 max_depth갑으로 인해 새 노드가 추가됨으로써 모순이 발생하면 추가하지 않음
    -- > 여기서 시간복잡도
    부모로 올라가면서 depth+1 하고 max_depth가 큰지 비교
    최대 깊이(100) 20000번  -> 해결 가능

2)색깔변경
    m_id를 루트로 하는 서브트리의 모든 노드 색을 지정색으로 변경

    최대 노드개수 2만개
    이 명령 최대 실행 5만번 -> dfs로는 불가능할듯
    -모든 노드를 바꿀 수 없음


3)색깔 조회 - 2만번이기 떄문 -> 높이만큼 연산은 할 수 있겠다는 힌트
    부모로 올라가서 가장 마지막에 바뀐 색을 추적하면 색을 파악할 수 있을 것.
    m_id의 현재 색깔 조회

4) 점수조회 - 100번 -> 모든 노드를 순회할 수 있겠다는 생각이 들어야함
    모든 노드의 가치 제곱의 합
    가치 - 해당 노드를 루트로 하는 서브트리 내 서로 다른 색깔의 수

    루트로 부터 순회를 하면서 모든 노드의 색을 구하기 가능
    -> 3번과 마찬가지로 내려가면서 마지막에 바뀐 색 추적 - 파악 가능
    가치 계산 - 노드마다 색깔 배열
    자식으로 부터 배열을 받아 구할 수 있음(재귀) - Tree DP
     -dp[i] : i를 루트로 했을 떄 서브트리 색 종류를 나타낸 상태 값

    or 비트연산을 이용하면 빠르다
    
'''
from collections import defaultdict
q = int(input())
nodes = {}


class Node:
    def __init__(self, m_id, parent, color, max_depth):
        self.m_id = m_id
        self.parent = parent
        self.color = color
        self.last_updated = turn
        self.max_depth = max_depth
        self.child = []
        
def can_create(node, h):
    if node.max_depth < h:
        return False
    return node.parent is None or can_create(node.parent, h+1)

def find_color(node):
    color = 0
    last_updated = 0
    while node is not None:
        if node.last_updated > last_updated:
            color = node.color
            last_updated = node.last_updated
        node = node.parent
    
    return color

def get_one(state):
    cnt = 0
    for i in range(1,6):
        if state & (1<<i):
            cnt += 1
    return cnt

def get_colors(node, color, last_updated): # 노드가 가지고 있는 서브트리의 색깔들 상태(비트계산 - 정수)
    if node.last_updated > last_updated:
        color = node.color
        last_updated = node.last_updated
    state = 1 << color
    for child in node.child:
        state |= get_colors(child,color,last_updated)

    #state에 있는 1의 개수의 제곱
    global answer
    answer += get_one(state) ** 2

    return state


for turn in range(1,q+1):
    cmd, *remain = map(int, input().split())
    if cmd == 100:
        m_id, p_id, color, max_depth = remain
        # 노드 추가할 수 있는지 확인
        
        parent = None if p_id == -1 else nodes[p_id]
        if parent is not None and not can_create(parent, 2):
            continue
        nodes[m_id] = Node(m_id, parent, color, max_depth)
        if parent is not None:
            parent.child.append(nodes[m_id])

    elif cmd == 200:
        m_id, color = remain
        node = nodes[m_id]
        node.color = color
        node.last_updated = turn
    elif cmd == 300:
        m_id = remain[0]
        print(find_color(nodes[m_id]))

    elif cmd == 400:
        answer = 0
        for node in nodes.values():
            if node.parent == None:
                get_colors(node,0,0)
        print(answer)
        
    
        
