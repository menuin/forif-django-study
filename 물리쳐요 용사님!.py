import random

class Hero:
    def __init__(self,name):
        self.name=name
        self.health=0
        self.gold=random.randint(200,500)
        self.weapon={}
        


    def buyweapon(self): 
        print("당신이 가진 돈 :",self.gold)
        newweapon=int(input("장비를 고르세요 : 1.돌_100원  2.칼_200원  3.총_300원 "))

        if newweapon==1 and self.gold>=100:
            self.gold-=100
            self.weapon['돌']=random.randint(1,100)
            self.health+=self.weapon['돌']

        elif newweapon==2  and self.gold>=200:
             self.gold-=200
             self.weapon['칼']=random.randint(100,300)
             self.health+=self.weapon['칼']

        elif newweapon==3 and self.gold>=300:
            self.gold-=300
            self.weapon['총']=random.randint(300,500)
            self.health+=self.weapon['총']

        else:
            print("돈이 부족하거나 없는 선택지입니다")
            return
       
        print("가진 돈 :",self.gold,"체력 :",self.health, "가진 무기 :",self.weapon)
        


    def play(self):
        print("랜덤한 몬스터가 나타났다!")
        monsterhealth=random.randint(100,500)

        print("내 공격력 :",self.health, "몬스터의 공격력 :",monsterhealth)

        if self.health>monsterhealth:
            print("성공!")

        else:
            print("실패!")
        
