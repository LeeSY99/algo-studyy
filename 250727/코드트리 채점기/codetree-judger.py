'''
1 채점기 준비
    n개
    u_0 - url (도메인/문제id)
    1~n번호 - 0초에 우선순위 1이면서 url이 u_0인 초기문제 채점
    
2 채점요청
    t초에 우선순위 p이면서 u 요청 들어옴
    대기 큐에 있는 task중 u와 일치하는 url이 단 하나라도 존재하면 큐에 추가하지 않고 넘어감
    
3 채점 시도
    대기 큐에서 즉시 불가능한 제외하고 남은 것들중 가장 우선순위 높은 것 채점
    채점이 될 수 없는 조건
        현재 채점 중
        가장 최근에 진행된 채점 시작 시간 start, 종료 start + gap
        현재 시간 t가 start + 3*gap  보다 작음

    우선순위
        p번호가 작을수록
        대기 큐에 빨리 들어옴\

4 채점 종료
    t초에 J_id 채점기가 진행하던 채점이종료 -> 쉬는 상태
    j_id 채점기가 진행하던 채점이 없었으면 무시

5. 채점 대기 큐 조회
         '''

import heapq
waiting_url = set()
waiting_q = {}
now_scoring_domains = set()
domain_history = {}
valid_score_machine = []
score_machine = []


q = int(input())
class Task:
    def __init__(self, url, p, in_time):
        self.url = url
        self.p = p
        self.in_time = in_time

        self.score_start = -1
        self.score_end = -1


        domain, p_id = url.split('/')
        self.domain = domain
        self.id = int(p_id)

    def __lt__(self, other):
        if self.p != other.p:
            return self.p < other.p
        if self.in_time != other.in_time:
            return self.in_time < other.in_time

class History:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def valid(self,t):
        gap = self.end - self.start
        return t >= self.start + 3*gap


def do_100():
    global waiting_url,waiting_q ,now_scoring_domains,domain_history,valid_score_machine,score_machine
    n, u_0 = remain
    n = int(n)
    task = Task(u_0,1,0)
    waiting_url.add(u_0)
    heapq.heappush(waiting_q.setdefault(task.domain,[]), task)  #도메인별로 힙을 설정하고 거기에 task 객체를 넣음 -> O(n)에서 O(300)
    valid_score_machine = [i for i in range(1,n+1)]
    score_machine = [None] * (n+1)

def do_200(p, url, t):
    global waiting_url,waiting_q ,now_scoring_domains,domain_history,valid_score_machine,score_machine
    if url in waiting_url:
        return
    task = Task(url,p,t)
    waiting_url.add(url)
    heapq.heappush(waiting_q.setdefault(task.domain,[]),task)

def is_domain_scoreable(time,domain):
    if domain in now_scoring_domains:
        return False
    
    history = domain_history[domain] if domain in domain_history else None
    if history and not history.valid(time):
        return False
    return True
    

def do_300(t):
    global waiting_url,waiting_q ,now_scoring_domains,domain_history,valid_score_machine,score_machine
    if not valid_score_machine:
        return
    
    best_task = None
    for domain, task_heapq in waiting_q.items():
        if not task_heapq or not is_domain_scoreable(t,domain): 
            continue
        if not best_task or task_heapq[0]<best_task:
            best_task = task_heapq[0]
    if not best_task:
        return
    
    j_id = heapq.heappop(valid_score_machine)
    best_task.score_start = t
    
    heapq.heappop(waiting_q[best_task.domain])
    now_scoring_domains.add(best_task.domain)
    score_machine[j_id] = best_task
    waiting_url.remove(best_task.url)

def do_400(t, j_id):
    global waiting_url,waiting_q ,now_scoring_domains,domain_history,valid_score_machine,score_machine
    end_task: Task | None = score_machine[j_id]
    if not end_task:
        return
    
    end_task.score_end = t

    now_scoring_domains.remove(end_task.domain)
    score_machine[j_id] = None
    heapq.heappush(valid_score_machine, j_id)
    domain_history[end_task.domain] = History(end_task.score_start,end_task.score_end)

def do_500(t):
    global waiting_url,waiting_q ,now_scoring_domains,domain_history,valid_score_machine,score_machine
    print(len(waiting_url))




for time in range(q):
    to_do, *remain = input().split()
    to_do = int(to_do)
    if to_do == 100:
        do_100()
    elif to_do == 200:
        t, p, u = remain
        do_200(int(p), u, int(t))
    elif to_do == 300:
        t = remain[0]
        do_300(int(t))
    elif to_do == 400:
        t, j_id = remain
        do_400(int(t),int(j_id))
    elif to_do == 500:
        t = remain[0]
        do_500(int(t))

 