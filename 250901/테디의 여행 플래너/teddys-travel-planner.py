N,Q = map(int, input().split())
city = list(input().split())
class City:
    def __init__(self,name):
        self.name = name
        self.next = None
        self.prev = None
#첫도시가 핀셋
class Dlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_back(self, city):
        if self.count == 0:
            self.head = city
            self.tail = city
        else:
            self.tail.next = city
            city.prev = self.tail
            self.tail = city
        
        self.tail.next = self.head
        self.head.prev = self.tail
        self.count += 1

    def delete_back(self,pin):
        target = pin.next
        if self.count == 1:
            return
        
        if target == self.tail:
            target.prev.next = None
            self.tail = pin
        elif target == self.head:
            self.head = target.next

        pin.next = target.next
        target.next.prev = pin

        target.next = None
        target.prev = None
        self.count -= 1
        self.head.prev = self.tail
        self.tail.next = self.head

    def add_back_pin(self,pin,city):
        if pin == self.tail:
            pin.next = city
            city.prev = pin
            self.tail = city
        
        else:
            pin.next.prev = city
            city.next = pin.next
            pin.next = city
            city.prev = pin
        self.count += 1
        self.tail.next = self.head
        self.head.prev = self.tail
            


trip = Dlist()
for c in city:
    new_city = City(c)
    trip.add_back(new_city)
pin = trip.head


for _ in range(Q):
    cmd , *r = input().split()

    if cmd == '1':
        if pin.next:
            pin = pin.next
    elif cmd == '2':
        if pin.prev:
            pin = pin.prev

    elif cmd == '3':
        if pin.next:
            trip.delete_back(pin)


    elif cmd == '4':
        new_city = City(r[0])
        trip.add_back_pin(pin, new_city)


    if pin.prev:
        prev_city = pin.prev
    else:
        prev_city = trip.tail
    
    if pin.next:
        next_city = pin.next
    else:
        next_city = trip.head

    if prev_city.name == next_city.name:
        print(-1)
    else:
        print(prev_city.name, next_city.name)

    