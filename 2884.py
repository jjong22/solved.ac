hour, mins = map(int,input().split())

if(mins >= 45):
    print(hour, mins-45)
elif (mins < 45):
    if (hour != 0 ):
        print(hour - 1, mins + 15)
    else :
        print(24 - 1, mins + 15)