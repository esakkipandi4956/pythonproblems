class numbers():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
class addition(numbers):
    def add(self):
        add=self.num1+self.num2
        print(f"The addition of {self.num1} + {self.num2} is:",add)
class multiply(addition):
    def multi(self):
        multi=self.num1*self.num2
        print(f"The multiplication of {self.num1} * {self.num2} is:",multi)
class divide(multiply):
    def div(self):
        div=self.num1/self.num2
        print(f"The division of {self.num1} / {self.num2} is:",div)
class modulo(divide):
    def mod(self):
        mod=self.num1%self.num2
        print(f"The modulo of {self.num1} % {self.num2} is:",mod)
a=int(input())
b=int(input())
obj1=modulo(a,b)
obj1.add()
obj1.multi()
obj1.div()
obj1.mod()
