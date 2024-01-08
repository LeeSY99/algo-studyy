day_of_month=[0,31,29,31,30,31,30,31,31,30,31,30,31]

m1,d1,m2,d2=map(int,input().split())
A=input()

start_day=0
for i in range(m1):
    start_day+=day_of_month[i]
start_day+=d1

end_day=0
for i in range(m2):
    end_day+=day_of_month[i]
end_day+=d2


if A=='Tue':
    start_day+=1
elif A=='Wed':
    start_day+=2
elif A=='Thu':
    start_day+=3
elif A=='Fri':
    start_day+=4
elif A=='Sat':
    start_day+=5
elif A=='Sun':
    start_day+=6

gap=end_day-start_day

count=gap//7
print(count+1)