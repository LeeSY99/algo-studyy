''' n*n격자 각 격자에는 무기가 있을 수 있음
초기에는 빈 격자에 플레이어들이 위치, 초기 능력치 가짐(다 다름)
빨간색 숫자 -> 총일떈 공격력, 플레이어의 경우 초기 능력치
노란 숫자 -> 플레이어 번호
플레이어 (번호, 위치, 초기 능력치, 총) -> 단순한 객체가 아닌 정보가 좀 있으면 class로 하면 좋다

k*m*m
1라운드 (총 k라운드) (k)
    모든 플레이어(1~n번 플레이어) (m)
        1칸 이동(벽이있으면 반대로)
        플레이어가 없으면 (m)
            바닥의 총들과 비교해 총 교체
        플레이어가 있으면
            싸움 (초기능력치 + 총의 공격력 이 높은 사람 이김, 같으면 초긴능력치가 높은 플레이어가 이김)
            이긴사람 : 포인트 획득(초기능력치 총의 공력력의 차이)
            진사람 : 총 내려놓고 1칸 이동.
                이동할 칸에 다른 플레이어가 있거나 격자 밖이면 90도 회전하면서 갈 수 있는 곳 찾기
                이동 후 총이 있으면 총 획득
            이긴사람: 총 춥기'''

def in_range(r,c):
    return 0<=r<n and 0<=c<n

class Player:
    #i 번호
    #x,y 좌표
    #d 방향
    #s 초기 능력치
    #a 가진 총의 공격력
    #point
    def __init__(self, i, x, y, d, s, a, point):
        self.i = i
        self.x = x
        self.y = y
        self.d = d
        self.s = s
        self.a = a
        self.point = 0
    
    def move(self):
        nx, ny = self.x + dxs[self.d], self.y + dys[self.d]
        if not in_range(nx,ny):
            self.d = (self.d+2) % 4
        self.x, self.y = self.x + dxs[self.d], self.y + dys[self.d]

    def change_gun(self):
        #플레이어의 위치에 총이 있을 경우
        if len(guns[self.x][self.y]) == 0:
            return
        max_a = max(guns[self.x][self.y])
        if self.a > max_a:
            return
        guns[self.x][self.y][guns[self.x][self.y].index(max_a)] = self.a
        self.a = max_a

    def drop_gun(self):
        guns[self.x][self.y].append(self.a)
        self.a = 0
            
            

def fight(player1, player2):
    if player1.s + player1.a == player2.s + player2.a:
        if player1.s > player2.s:
            return player1, player2
        else:
            return player2, player1
    elif player1.s + player1.a > player2.s + player2.a:
        return player1, player2
    else:
        return player2, player1

n,m,k = map(int,input().split())

guns = [[[] for _ in range(n)] for _ in range(n)]

for x in range(n):
    row = list(map(int, input().split()))
    for y, item in enumerate(row):
        if item != 0:
            guns[x][y].append(item)
dxs, dys = [-1,0,1,0], [0,1,0,-1] 

#player(x,y,d,s)
players = []
for i in range(m):
    x,y,d,s = map(int,input().split())
    players.append(Player(i,x-1,y-1,d,s,0,0))

for r in range(k):
    for player in players:
        player.move()
        another_player = list(filter(lambda p : (player.x,player.y) == (p.x, p.y) and player.i != p.i, players))
        if another_player:
            winner, loser = fight(player, another_player[0])
            winner.point += (winner.s + winner.a - loser.s - loser.a)
            loser.drop_gun()
            for ii in range(4):
                nx, ny = loser.x + dxs[(loser.d+ii)%4], loser.y + dys[(loser.d+ii)%4]
                if in_range(nx,ny) and len(list(filter(lambda p: (p.x, p.y) == (nx,ny), players))) == 0:
                    loser.x = nx
                    loser.y = ny
                    loser.d = (loser.d+ii) %4
                    break
            loser.change_gun()
            winner.change_gun()
            
        else:
            player.change_gun()

for player in players:
    print(player.point, end = ' ')
