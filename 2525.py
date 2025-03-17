hour, mins = map(int,input().split())
time = int(input())
up1 = int()
up2 = int()

if(mins + time < 60):
    print(hour, mins + time)
elif (mins + time >= 60):
    up1 = int((mins + time) / 60)
    up2 = int((hour + up1) / 24)
    if (hour + up1 >= 24):
        print((hour + up1) - up2 * 24, (mins + time)- (up1 * 60))
    else :
        print(hour + up1, (mins + time)- (up1 * 60))
