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

for i in range(n):
    name, addr, city = input().split()
    person = info(name,addr,city)
    if i == n-1:
        person.print_info()
