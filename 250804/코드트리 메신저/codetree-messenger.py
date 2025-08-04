''' 이진트리 
최상단 - 메인채팅방
자식 - 부서별 채팅방

1) 사내매신저 준비
    0~n번 n+1개 채팅방, 메인채팅방 제외 모두 부모 존재
    메인: 0번
    각 채팅방 부모 채팅방 번호: parents

    각 채팅방은 권한을 가짐
        c번 채팅방에서 메세지를 보내면 상위 채팅방들에게 알림
        authority_C만큼만 위로 올라감

2) 알람망 설정 온/오프
    맨처음은 다 켜져있음
    기능이 작동되면 on->off, off->on
    off상태면 자기자신을 포함해 위로 알림을 보내지 않음

3)권한 세기 변경
    c번 채팅방의 권한 세기를 power로 변경

4) 부모 채팅방 교환
    c1, c2채팅방의 부모를 서로 바꿈

5) 알림을 받을 수 있는 채팅방 수 조회
    c번 채팅방까지 알림이 도달할 수 있는 서로 다른 채팅방 수 출력
'''
MAX_DEPTH = 20

n, q = map(int, input().split())
class Chat:     
    def __init__(self,parent=None,power=None):
        self.parent = parent
        self.power = min(power,MAX_DEPTH)
        self.alarm_on = True
        self.D = [0] * (MAX_DEPTH+1)
        self.D[self.power] += 1

chats = [] 
root = None

def make_chat_room():
    global root, chats, tree
    parents = [0] + remain[:n]
    authority = [0] + remain[n:]
    # root = Root()
    for i in range(n+1):
        chats.append(Chat(parents[i],authority[i]))

    tree = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        tree[parents[i]].append(i)

    dfs(0)

def update_path(start_idx, coeff):
    global n, chats
    start = chats[start_idx]
    target_idx = start_idx
    target = chats[target_idx]
    depth = 0
    while 1:
        if not target.alarm_on or target_idx == 0:
            break
        target_idx = target.parent
        target = chats[target_idx]
        depth +=1

        for power in range(depth, MAX_DEPTH + 1):
            target.D[power - depth] += start.D[power] * coeff

tree = []
def dfs(idx):
    global tree

    update_path(idx, coeff=1)

    for child_idx in tree[idx]:
        dfs(child_idx)


def on_off(idx):
    global chats

    update_path(idx, coeff = -1)
    chats[idx].alarm_on = not chats[idx].alarm_on
    update_path(idx, coeff = 1)

def change_power(idx, power):
    global MAX_DEPTH
    power = min(MAX_DEPTH,power)

    update_path(idx, coeff = -1)
    chats[idx].D[chats[idx].power] -=1
    chats[idx].power = power
    chats[idx].D[chats[idx].power] +=1
    update_path(idx, coeff = 1)

def change_parent(idx_a, idx_b):
    global chats

    update_path(idx_a, coeff=-1)
    update_path(idx_b, coeff=-1)

    chats[idx_a].parent, chats[idx_b].parent = chats[idx_b].parent, chats[idx_a].parent

    update_path(idx_a, coeff=1)
    update_path(idx_b, coeff=1)
    
            
def count_chats(idx):
    print(sum(chats[idx].D)-1)

# direction, *remain = map(int,input().split())
# if direction == 100:
#     make_chat_room()

def print_tree():
    print(root.left.chat_num)
    if root.right: print(root.right.chat_num)
    print('-----')
    for i in range(1,n+1):
        print(f'node: {i}')
        node = chats[i]
        if node.left:
            print(f'left: {node.left.chat_num}')
        if node.right:
            print(f'right: {node.right.chat_num}')


for _ in range(q):
    direction, *remain = map(int,input().split())
    if direction == 100:
        make_chat_room()
        # print_tree()
    elif direction == 200:
        # pass
        c = remain[0]
        on_off(c)
    elif direction == 300:
        # pass
        c, power = remain[0], remain[1]
        change_power(c, power)
    elif direction == 400:
        # pass
        c1, c2 = remain[0], remain[1]
        change_parent(c1, c2)
    elif direction == 500:
        # pass
        c=remain[0]
        count_chats(c)
