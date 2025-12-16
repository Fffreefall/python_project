from calculator import Calculator

calc = Calculator()
# res=calculator.sum(1,5)
# assert res == 10
res = calc.sum(4, 5)
assert res == 9
res = calc.sum(-6, -10)
assert res == -16
res = calc.sum(-6, 6)
assert res == 0