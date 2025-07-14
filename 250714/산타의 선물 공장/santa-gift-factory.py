'''
공장에서 순서대로q개의 명령에 따라 일을 진행
일의 종류는 5가지
1. 공장 설립
    공장에 m개의 벨트를 설치하고, 각 벨트 위에 정확히 n/m개의 물건을 놓음
    총 n개의 물건 준비
    각 물건에는 id와 무게가 적힘
    번호는 다 다름, 무게는 같을 수 잇음
2. 물건 하차
    w_max: 산타가 원하는 최대 무게
    순서대로 벨트를 보면서 맨 앞의 상자가 w_max이하면 하차
    아니면 벨트 맨 뒤로 보냄
    하차된 상자 무게 합 출력
3. 물건 제거
    제거할 상자 번호 r_id 제거
    나머지 상자는 한칸 앞으로
    상자가 있으면 해당 r_id, 업으면 -1 출력

4. 물건 확인 f_id
    해당 번호의 상자가 놓여있는 벨트의 번호 출력, 없으면 -1
    상자가 있을때는 해당 상자와 뒤에 있는 모든 상자를 맨 앞으로 가져옴(순서는 그대로 유지)

5. 벨트 고장 b_num
    고장난 벨트 오른쪽부터 순서대로 보면서 고장이 나지 않은 최초의 벨트 위로 상자를 앞에서 부터 옮김

'''
class Box:
    def __init__(self, id, weight):
        self.next = None
        self.prev = None
        self.box_id = id
        self.weight = weight

class Belt:
    def __init__(self):
        self.head = None
        self.tail = None
        self.boxes = 0

    def push_front(self,id,weight):
        new_box = Box(id,weight)
        
        #빈 벨트에 상자 놓음
        if self.head == None:
            self.head = new_box
            self.tail = new_box
            new_box.next = None
            new_box.prev = None
        else:
            new_box.next = self.head
            self.head.prev = new_box
            self.head = new_box
            new_box.prev = None
        self.boxes += 1

    def push_back(self,id,weight):
        new_box = Box(id,weight)
        # empty belt
        if self.tail == None:
            self.tail = new_box
            self.head = new_box
            new_box.next = None
        else:
            self.tail.next = new_box
            new_box.prev = self.tail
            self.tail = new_box
            new_box.next = None
        self.boxes += 1

    def pop_front(self):
        temp = self.head
        if temp.next == None:
            self.head = None
            self.tail = None
            self.boxes = 0
        else:
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.boxes -= 1
        return temp

    def pop_back(self):
        temp = self.tail
        if temp.prev == None:
            self.head = None
            self.tail = None
            self.boxes = 0
        else:
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.boxes -= 1
        return temp

    def remove_box(self, r_id):
        now_node = self.head
        while now_node != None:
            if now_node.box_id == r_id:
                if now_node == self.head:
                    self.head.next.prev = None
                    self.head.next = None
                    self.head = self.head.next
                elif now_node == self.tail:
                    self.tail.prev.next = None
                    self.tail.prev = None
                    self.tail = self.tail.prev
                else:
                    now_node.prev.next = now_node.next
                    now_node.next.prev = now_node.prev
                    now_node.next = None
                    now_node.prev = None
                return r_id
            now_node = now_node.next
        return -1

    def all_back(self,f_id):
        while 1:
            now_box = self.pop_back()
            # print(now_box.box_id, now_box.weight)
            self.push_front(now_box.box_id, now_box.weight)
            if now_box.box_id == f_id:
                break
                
            
def box_off(w_max):
    all_weight = 0
    for i,belt in enumerate(belts):
        if belt_on[i] == 0:
            continue
        now_box = belt.pop_front()
        if now_box.weight <= w_max:
            all_weight += now_box.weight
        else:
            belt.push_back(now_box.box_id, now_box.weight)
    return all_weight

def remove(r_id):
    for i,belt in enumerate(belts):
        if belt_on[i] == 0:
            continue
        result = belt.remove_box(r_id)
        if result > 0:
            return result
    return -1

def check(f_id):
    for i, belt in enumerate(belts):
        now_node = belt.head
        while now_node != None:
            if now_node.box_id == f_id:
                return i+1, belt
            now_node = now_node.next
    return -1, belt





q = int(input())


# direction = list(map(int,input().split()))
# to_do = int(direction[0])
# if to_do == 100:
#     n, m = int(direction[1]), int(direction[2])
#     belt_on = [1] * m
#     box_info = direction[3:3+n]
#     box_weight = direction[3+n:]
#     boxes_per_belt = n//m
#     belts = [Belt() for _ in range(m)]
#     for i in range(n):
#         belt_no = i//boxes_per_belt
#         new_id = box_info[i]
#         new_weight = box_weight[i]
#         belts[belt_no].push_back(new_id,new_weight)

def print_belt(that_belt):
    belt = that_belt
    box = belt.head
    while box !=None:
        print(box.box_id, box.weight)
        box=box.next
def print_all():
    for belt in belts:
        box = belt.head
        while box !=None:
            print(box.box_id, box.weight)
            box=box.next
        print('---')


# print(belts)

for _ in range(q):
# for _ in range(6):
    direction = list(map(int,input().split()))
    to_do = int(direction[0])
    if to_do == 100:
        n, m = int(direction[1]), int(direction[2])
        belt_on = [1] * m
        box_info = direction[3:3+n]
        box_weight = direction[3+n:]
        boxes_per_belt = n//m
        belts = [Belt() for _ in range(m)]
        for i in range(n):
            belt_no = i//boxes_per_belt
            new_id = box_info[i]
            new_weight = box_weight[i]
            belts[belt_no].push_back(new_id,new_weight)
        # print_all()
    
    elif to_do == 200:
        w_max = direction[1]
        print(box_off(w_max))
        # print_all()
    elif to_do == 300:
        r_id = direction[1]
        result = remove(r_id)
        print(result)
        # print_all()
    elif to_do == 400:
        f_id = direction[1]
        belt_no, that_belt = check(f_id)
        if belt_no == -1:
            print(belt_no)
        else:
            print(belt_no)
            that_belt.all_back(f_id)
            # print_all()
    elif to_do == 500:
        b_num = direction[1]
        b_num -= 1
        if belt_on[b_num] == 0:
            print(-1)
        else:
            belt_on[b_num] = 0
            for ii in range(m):
                if belt_on[(b_num + ii) % m] == 1:
                    on_belt = belts[(b_num + ii) % m]
                    break
            broken_belt = belts[b_num]
            while broken_belt.boxes != 0:
                move_box = broken_belt.pop_front()
                on_belt.push_back(move_box.box_id, move_box.weight)
            print(b_num+1)
            


        
        
