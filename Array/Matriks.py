'''
This code was created by Robanu Dakhayin
'''

# Import library
from random import randint

class Matriks :

    # Constructor
    def __init__(self, i= None, j= None) :
        if(type(i) == list) : self.__matriks = i
        elif(i != None and j != None) :
            self.__matriks = []
            for k in range(i) : self.__matriks.append([])
            for baris in range(i) :
                for kolom in range(j) :
                    self.__matriks[baris].append(randint(a= 0, b= 100))
        elif(i != None) : self.__init__(i= i, j= i)
        elif(j != None) : self.__init__(i= j)
        else : self.__init__(i= randint(a= 1, b= 5),j= randint(a= 2, b= 5))

    # Method jumlah2Matriks -> sum matriks
    def jumlah2Matriks(self, matriks1, matriks2= None) :
        if(matriks2 == None) :
            m1 = self.__matriks.copy()
            if(type(matriks1) == list) : m2 = matriks1.copy()
            elif(type(matriks1) == Matriks) : m2 = matriks1.__matriks.copy()
            else : m2 = Matriks(matriks1).__matriks.copy()
        else : 
            m1 = matriks1.copy() if(type(matriks1) == list) else matriks1.__matriks.copy() if(type(matriks1) == Matriks) else Matriks(matriks1).__matriks.copy()
            m2 = matriks2.copy() if(type(matriks2) == list) else matriks2.__matriks.copy() if(type(matriks2) == Matriks) else Matriks(matriks2).__matriks.copy()
        result = []
        for i in range(max(len(m1),len(m2))) : result.append([])
        for i in range(len(result)) : 
            if(i < min(len(m1),len(m2))) :
                for j in range(max(len(m1[i]),len(m2[i]))) : result[i].append(m1[i][j] + m2[i][j]) if(j < min(len(m1[i]),len(m2[i]))) else result[i].append(m1[i][j]) if (len(m1[i]) == max(len(m1[i]),len(m2[i]))) else result[i].append(m2[i][j])
            else :
                if(len(result) == len(m1)) : 
                    for num in m1[i] : result[i].append(num)
                else :
                    for num in m2[i] : result[i].append(num)
        return result
        
    # Method overloading selisih2Matriks
    def selisih2Matriks(self, matriks1, matriks2= None) :
        if(matriks2 == None) :
            m1 = self.__matriks.copy()
            if(type(matriks1) == list) : m2 = matriks1.copy()
            elif(type(matriks1) == Matriks) : m2 = matriks1.__matriks.copy()
            else : m2 = Matriks(matriks1).__matriks.copy()
        else : 
            m1 = matriks1.copy() if(type(matriks1) == list) else matriks1.__matriks.copy() if(type(matriks1) == Matriks) else Matriks(matriks1).__matriks.copy()
            m2 = matriks2.copy() if(type(matriks2) == list) else matriks2.__matriks.copy() if(type(matriks2) == Matriks) else Matriks(matriks2).__matriks.copy()
        result = []
        for i in range(max(len(m1),len(m2))) : result.append([])
        for i in range(len(result)) : 
            if(i < min(len(m1),len(m2))) :
                for j in range(max(len(m1[i]),len(m2[i]))) : result[i].append(m1[i][j] - m2[i][j]) if(j < min(len(m1[i]),len(m2[i]))) else result[i].append(m1[i][j]) if (len(m1[i]) == max(len(m1[i]),len(m2[i]))) else result[i].append((-1) * m2[i][j])
            else :
                if(len(result) == len(m1)) : 
                    for num in m1[i] : result[i].append(num)
                else :
                    for num in m2[i] : result[i].append(num)
        return result
    

    # Method tampilMatriks -> show matriks
    def tampilMatriks(self, matriks= None) : 
        m = self.__matriks if(matriks == None) else matriks if(type(matriks) == list) else matriks.__matriks if(type(matriks) == Matriks) else [[matriks]]
        for row in range(len(m)) :
            for col in range(len(m[row])) :
                print(m[row][col],end="\t")
            print()


# Test Class

# Create object
operator = Matriks()
obj1 = Matriks()
obj2 = Matriks(i= 3)
obj3 = Matriks(j= 3)
obj4 = Matriks([[1,2],[3,4]])
obj5 = Matriks(i= 3,j= 4)

# Call method jumlah2Matriks
print("obj1 =")
obj1.tampilMatriks()
print("obj2 =")
obj2.tampilMatriks()
sum1 = obj1.jumlah2Matriks(matriks1= obj2)
print("obj1 + obj2 = ")
operator.tampilMatriks(matriks= sum1)
sum2 = operator.jumlah2Matriks(matriks1= obj1, matriks2= obj2)
print(f"obj1 + obj2 =")
operator.tampilMatriks(matriks= sum2)

print("obj2 =")
obj2.tampilMatriks()
print("obj3 =")
obj3.tampilMatriks()
sum3 = obj2.jumlah2Matriks(matriks1= obj3)
print("obj2 + obj3 = ")
operator.tampilMatriks(matriks= sum3)
sum4 = operator.jumlah2Matriks(matriks1= obj2, matriks2= obj3)
print(f"obj2 + obj3 =")
operator.tampilMatriks(matriks= sum4)

print("obj4 =")
obj4.tampilMatriks()
print("obj5 =")
obj5.tampilMatriks()
sum5 = obj4.jumlah2Matriks(matriks1= obj5)
print("obj4 + obj5 = ")
operator.tampilMatriks(matriks= sum5)
sum6 = operator.jumlah2Matriks(matriks1= obj4, matriks2= obj5)
print(f"obj4 + obj5 =")
operator.tampilMatriks(matriks= sum6)

# Call method selisih2Matriks
print("obj1 =")
obj1.tampilMatriks()
print("obj2 =")
obj2.tampilMatriks()
sel1 = obj1.selisih2Matriks(matriks1= obj2)
print("obj1 - obj2 = ")
operator.tampilMatriks(matriks= sel1)
sel2 = operator.selisih2Matriks(matriks1= obj1, matriks2= obj2)
print(f"obj1 - obj2 =")
operator.tampilMatriks(matriks= sel2)

print("obj2 =")
obj2.tampilMatriks()
print("obj3 =")
obj3.tampilMatriks()
sel3 = obj2.selisih2Matriks(matriks1= obj3)
print("obj2 - obj3 = ")
operator.tampilMatriks(matriks= sel3)
sel4 = operator.selisih2Matriks(matriks1= obj2, matriks2= obj3)
print(f"obj2 - obj3 =")
operator.tampilMatriks(matriks= sel4)

print("obj4 =")
obj4.tampilMatriks()
print("obj5 =")
obj5.tampilMatriks()
sel5 = obj4.selisih2Matriks(matriks1= obj5)
print("obj4 - obj5 = ")
operator.tampilMatriks(matriks= sel5)
sel6 = operator.selisih2Matriks(matriks1= obj4, matriks2= obj5)
print(f"obj4 - obj5 =")
operator.tampilMatriks(matriks= sel6)