n=int(input())

honor='ABC'

def get_status(sa,sb,sc):
    score=[sa,sb,sc]
    max_score=(max(sa,sb,sc))
    winner=''
    for i in range(3):
        if score[i]==max_score:
            winner+=str(i)
    return winner
        

score_a,score_b,score_c=0,0,0
count=0

previous_honor='ABC'
for i in range(n):
    p, s=input().split()
    if p=="A":
        score_a += int(s)
    elif p=="B":
        score_b += int(s)
    elif p=="C":
        score_c += int(s)
    
    now_honor = get_status(score_a,score_b,score_c)
    if previous_honor!=now_honor:
        count+=1
        previous_honor=now_honor
print(count)