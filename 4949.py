while(1):
    sentence = input()
    if (sentence == "."):
        break
    
    partition = []
    result = True
    
    for char in sentence:
        if char == "[" or char == "(":
            partition.append(char)
        if char == "]" or char == ")":
            try:
                temp = partition.pop()
                if (char == "]" and temp == "["):
                    pass
                elif (char == ")" and temp == "("):
                    pass
                else:
                    result = False
                    break
            except:
                result = False
                break
                
    if (len(partition) != 0):
        result = False
    
    if (result == True):
        print("yes")
    else:
        print("no")