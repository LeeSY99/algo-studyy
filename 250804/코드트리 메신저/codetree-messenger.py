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

n, q = map(int, input().split())
class Root:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.chat_num = 0

class Chat:     
    def __init__(self,num,parent=None,auth=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.chat_num = num
        self.auth = auth
        self.alarm_on = True

chats = [None] * (n+1)
root = None

def make_chat_room():
    global root, chats
    parents = [0] + remain[:n]
    authority = [0] + remain[n:]
    # root = Root()
    chats[0] = Chat(0,None,0)
    for i in range(1,n+1):
        parent = parents[i]
        auth = authority[i]

        new_chat = Chat(i,parent,auth)
        chats[i] = new_chat

    for i in range(1,n+1):
        parent = chats[i].parent
        if chats[parent].left is None:
            chats[parent].left = chats[i]
        else:
            chats[parent].right = chats[i]

def on_off():
    c = remain[0]
    chats[c].alarm_on = not chats[c].alarm_on

def change_power():
    c = remain[0]
    power = remain[1]
    chats[c].auth = power

def change_parent():
    c1,c2 = remain[0], remain[1]
    c1_chat = chats[c1]
    c2_chat = chats[c2]
    p1_idx = c1_chat.parent
    p2_idx = c2_chat.parent
    c1_chat_parent = chats[c1_chat.parent]
    c2_chat_parent = chats[c2_chat.parent]

    if c1_chat_parent.left == c1_chat:
        c1_chat_parent.left = c2_chat
    else:
        c1_chat_parent.right = c2_chat
    
    if c2_chat_parent.left == c2_chat:
        c2_chat_parent.left = c1_chat
    else:
        c2_chat_parent.right = c1_chat

    c1_chat.parent, c2_chat.parent = p2_idx, p1_idx
    

def dfs(i, depth):
    global count, chats
    chat = chats[i]

    if depth <= chat.auth:
        count += 1

    if chat.left is not None and chat.left.alarm_on:
        dfs(chat.left.chat_num, depth + 1)

    if chat.right is not None and chat.right.alarm_on:
        dfs(chat.right.chat_num, depth + 1)

            
count = 0 
def count_chats():
    global count
    # dp = [0]*(n+1)
    c = remain[0]
    count = 0
    dfs(c,0)
    print(count-1)

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
        on_off()
    elif direction == 300:
        # pass
        change_power()
    elif direction == 400:
        # pass
        change_parent()
    elif direction == 500:
        # pass
        count_chats()
