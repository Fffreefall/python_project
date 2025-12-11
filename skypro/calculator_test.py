from calculator import Calculator
from training.skypro import calculator

# calculator = Calculator()
# res=calculator.sum(1,5)
# assert res == 10
res = calculator.sum(4,5)
assert res == 9
res = calculator.sum(-6,-10)
assert res == -16
res = calculator.sum(-6,6)
assert res == 0