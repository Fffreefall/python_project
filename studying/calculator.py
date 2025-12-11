class Calculator:
    #def __init__(self):

    def sum(self, a, b):
        result = a+b
        return result
    def sub(self, a, b):
        result = a-b
        return result
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0:
            raise ArithmeticError("На ноль делить нельзя")  # поднять ошибку
        return a/b
    def pow(self, a, b=2):
        return a**b
    def avg(self, nums):
        s=0
        for num in nums:
            s = s+num
        l = len(nums)
        return self.div(s, l)
