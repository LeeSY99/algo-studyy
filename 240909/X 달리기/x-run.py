x=int(input())

speed=[1]
moved=[1]
# 등차 수열의 합을 이용하여 구함
#속도를 올릴경우 이전속도를 v 라고 하면 (v+1)+(v)+...+2+1 을 이용하여 
#남은 거리가 더 많을 경우 속도를 올린다

#속도 유지도 비슷한 원리다
i=1
while(1):
    if (speed[i-1]+1) * (speed[i-1]+2) /2 <= x-moved[i-1]:
        now_speed=speed[i-1]+1
        speed.append(now_speed)
        moved.append(moved[i-1]+now_speed)
    elif (speed[i-1]) * (speed[i-1]+1) /2 <= x-moved[i-1]:
        now_speed=speed[i-1]
        speed.append(now_speed)
        moved.append(moved[i-1]+now_speed)
    else:
        now_speed=max(1,speed[i-1]-1) #중간에 속도가 0이되는걸 방지
        speed.append(now_speed)
        moved.append(moved[i-1]+now_speed)
    if moved[i]==x:
        break
    i+=1


print(len(moved))