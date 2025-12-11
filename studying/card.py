class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknown'
    def __init__(self, number, date, holder):
        self.number = number
        self.date = date
        self.holder = holder
    def pay(self, amount):
        print("с карты", self.number, "списали", amount)