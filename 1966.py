n = int(input())

for i in range(n):
    num_of_paper, to_search = map(int, input().split())
    num_list = list(map(int, input().split()))
    index_list = [j for j in range(num_of_paper)]
    
    while(1):
        if num_list[0] == max(num_list): # 최대값이면 출력
            if index_list[0] == to_search:
                print(num_of_paper - len(num_list) + 1)
                break
            else:
                num_list.pop(0)
                index_list.pop(0)
        else: # 최대값이 아니면 맨 뒤로 보내기
            num_list.append(num_list.pop(0))
            index_list.append(index_list.pop(0))