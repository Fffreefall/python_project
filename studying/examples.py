from user import User
from card import Card

alex = User("Alex") #экземпляр
card = Card("1234 5678 8765 4321", "03/28", "Alex F")

card.pay(1000)
alex.addCard(card)
alex.getCard().pay(1000)