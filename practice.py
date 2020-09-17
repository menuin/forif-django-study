class Account:
    def __init__(self, name, money):
        self.name=name
        self.money=money

    def deposit(self,amount):
        self.money+=amount
        print(f"{amount}원을 입금했습니다.")
        print("{}원을 입금해서 {}원이 되었습니다. ".format(amount,self.money))
