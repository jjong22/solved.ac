import sys
input = sys.stdin.readline
    
def intend(num):
    for i in range(num * 4):
        print("_", end="")    

def text0(num):
    intend(num)
    print("\"재귀함수가 뭔가요?\"")
    
def text1(num):
    intend(num)
    print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    
def text2(num):
    intend(num)
    print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    
def text3(num):
    intend(num)
    print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    
def text4(num):
    intend(num)
    print("라고 답변하였지.")

def answer(num):
    if (num == n):
        text0(num)
        intend(num)
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        text4(num)
    
    else : 
        text0(num)
        text1(num)
        text2(num)
        text3(num)
        
        answer(num+1)
    
        text4(num) 

n = int(input())   
cnt = 0

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
answer(0)
