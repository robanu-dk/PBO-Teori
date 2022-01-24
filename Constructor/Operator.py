'''
This code was created by Robanu Dakhayin
'''


class Operator :
    
    # Constructor
    def __init__(self, a= None, b= None) :
        if(a!= None and b!= None) :
            self.a = a
            self.b = b
        elif(a!= None) :
            self.a = a
            self.b = "" if(type(a) == str) else 0
        elif(b!= None) :
            self.a = "" if(type(b) == str) else 0
            self.b = b
        else :
            self.a = 0
            self.b = 0

    # Method add
    def __add__(self, other) :
        a = self.a
        b = self.b
        c = other.a
        d = other.b

        # Change data type of variable if there is variable with string data type
        for i in [self.a, self.b, other.a, other.b] :
            if(type(i) == str) :
                a = str(self.a)
                b = str(self.b)
                c = str(other.a)
                d = str(other.b)
                break
        return (a + c),(b + d)

    # Method subtraction
    def __sub__(self, other) :
        a = self.a
        b = self.b
        c = other.a
        d = other.b

        # Change data type of variable if there is variable with string data type
        for i in [self.a, self.b, other.a, other.b] :
            if(type(i) == str) :
                a = str(self.a)
                b = str(self.b)
                c = str(other.a)
                d = str(other.b)
                break
        
        # If the data type is String, then the last word will be subtracted, if the word is the same, otherwise there will be no subtraction
        if(type(a) == str) :
            a = a.removesuffix(c)
            b = b.removesuffix(d)
        else :
            a -= c
            b -= d
        return a, b


# Create object

# There is no string
print(">>> bil1 = Operator(a= 10, b= 45)")
bil1 = Operator(a= 10, b= 45)
print(">>> bil2 = Operator(a= 11, b= 9)")
bil2 = Operator(a= 11, b= 9)
print(">>> bil3 = Operator(a= 12)")
bil3 = Operator(a= 12)
print(">>> bil4 = Operator()")
bil4 = Operator()

# There is string
print(">>> bil5 = Operator(a= \"Aku berusia 20\",b = 2000)")
bil5 = Operator(a= "Aku berusia 20",b = 2000)
print(">>> bil6 = Operator(a= 20, b= 120)")
bil6 = Operator(a= 20, b= 120)
print(">>> bil7 = Operator(a= \"aku\")")
bil7 = Operator(a= "aku")

# add and display it
print(">>> print(bil1 + bil2)")
print(bil1 + bil2)

print(">>> print(bil1 + bil3)")
print(bil1 + bil3)

print(">>> print(bil1 + bil4)")
print(bil1 + bil4)

print(">>> print(bil3 + bil4)")
print(bil3 + bil4)

print(">>> print(bil5 + bil6)")
print(bil5 + bil6)

print(">>> print(bil5 + bil7)")
print(bil5 + bil7)

print(">>> print(bil6 + bil7)")
print(bil6 + bil7)

# subtraction and display it
print(">>> print(bil1 - bil2)")
print(bil1 - bil2)

print(">>> print(bil1 - bil3)")
print(bil1 - bil3)

print(">>> print(bil1 - bil4)")
print(bil1 - bil4)

print(">>> print(bil3 - bil4)")
print(bil3 - bil4)

print(">>> print(bil5 - bil6)")
print(bil5 - bil6)

print(">>> print(bil5 - bil7)")
print(bil5 - bil7)

print(">>> print(bil6 - bil7)")
print(bil6 - bil7)