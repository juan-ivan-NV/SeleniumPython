from f1 import A
from f2 import B

# multiple inheritance
# then single inheritance
class C(A):

    def __init__(self):
        print('This is child class constructor')

    def cclassmethod(self):
        print('This is C class funciton')