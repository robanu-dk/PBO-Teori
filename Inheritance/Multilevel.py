'''
This code was created by Robanu Dakhayin
'''

class Student :

    def __init__(self, rollNumber= None) :
        self.__rollNumber = int(rollNumber) if(rollNumber != None) else None

    def putNumber(self) : print(f"Roll Number = {self.__rollNumber}")

# Create child class of Student -> class Test
class Test(Student) :

    def __init__(self, sub1, sub2, rollNumber=None):
        super().__init__(rollNumber)
        self.__sub1, self.__sub2 = sub1, sub2

    def putMarks(self) :
        print(f"Nilai awal sub1 = {self.__sub1}")
        print(f"Nilai awal sub2 = {self.__sub2}")   

    def getSub1(self) : return self.__sub1

    def getSub2(self) : return self.__sub2 
    
# Create child class of Test -> Result
class Result(Test) :

    def __init__(self, sub1, sub2, rollNumber=None):
        super().__init__(sub1, sub2, rollNumber)

    def display(self) :
        total = super().getSub1() + super().getSub2()
        super().putNumber()
        super().putMarks()
        print(f"Total = {total}")

# Test Class

# Create object
student1 = Result(rollNumber= 1, sub1= 91, sub2= 99)
student2 = Result(sub1= 95, sub2= 97)

# Call method display
print("============================Student 1======================================")
student1.display()

print("============================Student 2======================================")
student2.display()