import random

mywin=0
robotwin=0
round=0

choices=['가위','바위','보']


while mywin!=3 and robotwin!=3:

    mychoice=input("가위, 바위, 보 중 하나를 선택하세요")
    robotchoice=random.randint(0,2)

    if choices.index(mychoice)-robotchoice==1 or robotchoice-choices.index(mychoice)==2:
        print("플레이어의 승리")
        mywin+=1
        round+=1

    elif robotchoice-choices.index(mychoice)==1 or choices.index(mychoice)-robotchoice==2:
        print("로봇의 승리")
        robotwin+=1
        round+=1

    else:
        print("무승부입니다")


    print("내 선택 :",mychoice,"로봇의 선택 :",choices[robotchoice])
    


if mywin==3:
    print("최종 : 플레이어의 승리")
else:
    print("최종 : 로봇의 승리")
