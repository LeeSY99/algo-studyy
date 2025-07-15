'''
공장에서 순서대로q개의 명령에 따라 일을 진행
일의 종류는 5가지






시간복잡도 
q * (공장설립(n) + 물건하차(m) + 물건제거(n) + 물건 확인)
q * ()
belts[i] - i번째 벨트를 linkedlist로 관리
box:
    box_id, weight, next, prev
Belt: 
    is_broken, head, tail, boxes
id_map[id]: hashmap box 조회
where[id]: 해당 box가 존재하는 벨트 조회

'''
class Box:
    def __init__(self, id, weight):
        self.next = None
        self.prev = None
        self.id = id
        self.weight = weight

class Belt:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0 #박스개수
        self.is_broken = False

    def push_back(self, box):
        if self.count == 0:
            self.head = box
            self.tail = box
            self.count += 1
            return

        self.tail.next = box
        box.prev = self.tail
        self.tail = box
        self.count += 1
    
    def pop_front(self):
        if self.count == 0:
            return
        if self.count == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.count -= 1
            return temp
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.count -= 1
            return temp

    def remove(self, box):
        if box == self.head:
            box.next.prev = None
            self.head = box.next
            box.next = None
        elif box == self.tail:
            box.prev.next = None
            self.tail = box.prev
            box.prev = None
        else:
            box.prev.next = box.next
            box.next.prev = box.prev
            box.next = None
            box.prev = None
        self.count -= 1

    def change(self, box):
        if box == self.head:
            return
        if box == self.tail:
            box.prev.next = None
            self.tail = box.prev
            self.head.prev = box
            box.next = self.head
            box.prev = None
            self.head = box
        else:
            self.head.prev = self.tail
            self.tail.next = self.head
            self.head = box
            self.tail = box.prev

            
            box.prev.next= None
            box.prev = None



q = int(input())



def print_belt(that_belt):
    belt = that_belt
    box = belt.head
    while box !=None:
        print(box.id, box.weight)
        box=box.next
def print_all():
    for belt in belts:
        box = belt.head
        while box !=None:
            print((box.id, box.weight), end = '->')
            box=box.next
        print()
    print('---')
def print_dict():
    for id, box in id_map.items():
        print(id, box.id, box.weight)
    print('---')


# print(belts)
id_map = {}
where = {}
for _ in range(q):
    direction = list(map(int, input().split()))
    to_do = direction[0]
    # '''1. 공장 설립
    # 공장에 m개의 벨트를 설치하고, 각 벨트 위에 정확히 n/m개의 물건을 놓음
    # 총 n개의 물건 준비
    # 각 물건에는 id와 무게가 적힘
    # 번호는 다 다름, 무게는 같을 수 잇음'''
    if to_do == 100:
        n, m = direction[1], direction[2]
        belts = [Belt() for _ in range(m)]
        for i in range(n):
            id = direction[3+i]
            weight = direction[3+i+n]
            box = Box(id, weight)
            belt_no = i // (n//m)
            id_map[id] = box
            where[id] = belt_no #0-based
            belts[belt_no].push_back(box)
        # print_all()

    # '''2. 물건 하차
    # w_max: 산타가 원하는 최대 무게
    # 순서대로 벨트를 보면서 맨 앞의 상자가 w_max이하면 하차
    # 아니면 벨트 맨 뒤로 보냄
    # 하차된 상자 무게 합 출력'''

    elif to_do == 200:
        w_max = direction[1]
        out_weight = 0
        for belt in belts:
            if belt.is_broken:
                continue
            first_box = belt.pop_front()
            if first_box.weight <= w_max:
                out_weight += first_box.weight
                id_map.pop(first_box.id)
                where.pop(first_box.id)

            else:
                belt.push_back(first_box)
        print(out_weight)
        # print_all()
        # print_dict()
    # '''
    # 3. 물건 제거 ## 보통 id를 주고 존재하는지 확인하려면 hashmap을 사용
    #     제거할 상자 번호 r_id 제거
    #     나머지 상자는 한칸 앞으로
    #     상자가 있으면 해당 r_id, 업으면 -1 출력'''
    elif to_do == 300:
        r_id = direction[1]
        if r_id not in id_map:
            print(-1)
        else:
            print(r_id)
            search_box = id_map[r_id]
            search_belt = belts[where[r_id]]
            # print(search_box.id, search_box.weight)
            search_belt.remove(search_box)
            id_map.pop(r_id)
            where.pop(r_id)
        # print_all()
            
    # '''4. 물건 확인 f_id
    # 해당 번호의 상자가 놓여있는 벨트의 번호 출력, 없으면 -1
    # 상자가 있을때는 해당 상자와 뒤에 있는 모든 상자를 맨 앞으로 가져옴(순서는 그대로 유지)'''
    elif to_do == 400:
        f_id = direction[1]
        if f_id not in where:
            print(-1)
        else:
            search_belt = where[f_id]
            print(search_belt+1)
            box = id_map[f_id]
            belts[search_belt].change(box)
#     '''5. 벨트 고장 b_num
#     고장난 벨트 오른쪽부터 순서대로 보면서 고장이 나지 않은 최초의 벨트 위로 상자를 앞에서 부터 옮김
# '''
    elif to_do == 500:
        b_num = direction[1]
        if belts[b_num-1].is_broken:
            print(-1)
        else:
            print(b_num)
            b_num-=1
            belts[b_num].is_broken = True
            for i in range(m):
                belt_num = (b_num + i)%m
                if not belts[belt_num].is_broken:
                    startbelt = belts[b_num]
                    endbelt = belts[belt_num]
                    while startbelt.count != 0:
                        move_box = startbelt.pop_front()
                        where[move_box.id] = belt_num
                        endbelt.push_back(move_box)


        



    
            


        
        

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