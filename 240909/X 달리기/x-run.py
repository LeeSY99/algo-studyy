x=int(input())

speed=[1]
moved=[1]

i=1
while(1):
    if (x//2) > moved[i-1]:
        now_speed=speed[i-1]+1
        speed.append(now_speed)
        moved.append((moved[i-1]+now_speed))
    else:
        now_speed=max(1,speed[i-1]-1)
        speed.append(now_speed)
        moved.append((moved[i-1]+now_speed))
    if moved[i]>=x:
        break
    i+=1

print(len(moved))