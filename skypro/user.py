
class User: #класс
    age = 0; #поле класса
    def __init__(self, name): #конструктор
        print("я создался")
        self.username = name #поле класса

    def sayName(self): #метод
        print("меня зовут ", self.username)
    def sayAge(self): #метод
        print(self.age)
    def setAge(self, newAge): #метод
        self.age = newAge
    def addCard(self, card):
        self.card = card
    def getCard(self):
        return self.card
