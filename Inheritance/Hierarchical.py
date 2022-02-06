'''
This code was created by Robanu Dakhayin
'''

class Shape : 

    def __init__(self, aName) -> None:
        self.__name = str(aName)
    
    def getName(self) -> str : return self.__name

    def calculateArea(self) -> float : return 0

# Create class Circle (child class of class Shape)
class Circle(Shape) : 

    def __init__(self, aName, r) -> None:
        super().__init__(aName)
        self.__radius = float(r)

    def calculateArea(self) -> float:
        return 3.14 * (self.__radius ** 2)

# Create class Square (child class of class Shape)
class Square(Shape) : 

    def __init__(self, aName, s) -> None:
        super().__init__(aName)
        self.__side = float(s)
    
    def calculateArea(self) -> float:
        return self.__side ** 2

# Test Class

# Create object
shape = Shape(aName= "Shape")
circle = Circle(aName= "Circle", r= 10)
square = Square(aName= "Square", s= 5)

# Call method calculateArea()
areaOfShape = shape.calculateArea()
areaOfCircle = circle.calculateArea()
areaOfSquare = square.calculateArea()

# Display
print("===============================Object Shape======================================")
print(f"Shape's name = {shape.getName()}")
print(f"Area of {shape.getName()} = {areaOfShape}")

print("===============================Object Circle======================================")
print(f"Shape's name = {circle.getName()}")
print(f"Area of {circle.getName()} = {areaOfCircle}")

print("===============================Object Square======================================")
print(f"Shape's name = {square.getName()}")
print(f"Area of {square.getName()} = {areaOfSquare}")
