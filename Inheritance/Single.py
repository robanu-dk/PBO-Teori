'''
This code was created by Robanu Dakhayin
'''

class B :

    def __init__(self, a, b) :
        self.__a, self.__b = a,b

    def getA(self) : return self.__a

    def getB(self) : return self.__b

    def showA(self) : print(f"a = {self.getA()}")

    def showB(self) : print(f"b = {self.getB()}")

# Class D merupakan child class dari class B
class D(B) :

    def __init__(self, a, b):
        super().__init__(a, b)

    def mul(self) : self.__c = super().getA() * super().getB()

    def dev(self) : self.__d = super().getB() / super().getA()

    def display(self) :
        super().showA()
        super().showB()
        print(f"c = {super().getA()} * {super().getB()} = {self.__c}")
        print(f"d = {super().getB()} / {super().getA()} = {self.__d}")

# Test class

# Create object
obj = D(a= 2, b= 9)    

# Call method mul and dev
obj.mul()
obj.dev()

# Call method display
obj.display()