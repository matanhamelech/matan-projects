from dataclasses import dataclass


@dataclass
class creditcard:
    money: int = 1000
    sum: int = 0
    time: int = 1
    ask: int = 0

    def __init__(self):
        for num in range(30):
            print(f'{self.time}/30')
            print("what do you want to do?")
            print("1.spend money")
            print("2.add money")
            self.ask = int(input())
            if self.ask == 1:
                self.spend_money()
            if self.ask == 2:
                self.add_money()
            self.time += 1
        print(f"you added {self.sum} money")

    def spend_money(self):
        self.x: int = int(input("how much money do you want to spend? "))
        self.money -= self.x
        print(f"spent {self.x} shekels")
        self.sum -= self.x

    def add_money(self):
        self.y: int = int(input("how much money do you want to add? "))
        self.money += self.y
        print(f"added {self.y} shekels")
        self.sum += self.y


clss = creditcard()
