while(1):
    name, old, weight = input().split()
    old = int(old)
    weight = int(weight)

    if name == '#' and old == 0 and weight == 0:
        break
    
    if old > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')