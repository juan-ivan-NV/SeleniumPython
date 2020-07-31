'''# First create a class
class A:

    def hello (self):
        print('Hi baby')

    def sum(self, a, b):
        c = a+b
        print('sum is - ' + str(c))
    
    def mul(self, a, b):
        c=a*b
        return c



# To call any member, create object of the class
obj = A()

# Call functions of class by using 
x = obj.mul(10,20)
print(x) '''

# Constructors
class A:
    def __init__(self, a, b):
        print('This is constructor')
        c = a+b
        print(c)
    
    def hello(self):
        print('Hy baby')
    
    def sum(self, a, b):
        c = a+b
        print('sum is - ' + str(c))
    
    def mul(self, a, b):
        c=a*b
        return c

obj = A(4,34)


