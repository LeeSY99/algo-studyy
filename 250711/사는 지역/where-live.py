class info:
    def __init__(self,name,addr,city):
        self.name=name
        self.addr=addr
        self.city=city
    
    def print_info(self):
        print(f'name {self.name}')
        print(f'addr {self.addr}')
        print(f'city {self.city}')

n = int(input())
people = []
for i in range(n):
    name, addr, city = input().split()
    person = info(name,addr,city)
    people.append(person)

people.sort(lambda x: x.name)
people[-1].print_info()
