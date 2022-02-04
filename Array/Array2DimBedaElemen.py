# Import library
from random import randint

class Array2DimBedaElemen :

    # Constructor
    def __init__(self, i= None, j= None) :
        if(type(i) == list) : self.__array2DimBedaElemen = i
        elif(i != None and j != None) :
            self.__array2DimBedaElemen = []
            for k in range(i) : self.__array2DimBedaElemen.append([])
            for baris in range(i) :
                for kolom in range(j[baris]) :
                    self.__array2DimBedaElemen[baris].append(randint(a= 0, b= 100))
        elif(i != None) : 
            kolom = []
            for k in range(i) : kolom.append(randint(a= 1,b= 5))
            self.__init__(i= i, j= kolom)
        else : pass

    # Method jumlah2Array2DimBedaElemen -> sum Array2DimBedaElemen
    def jumlah2Array2DimBedaElemen(self, array2DimBedaElemen1, array2DimBedaElemen2= None) :
        if(array2DimBedaElemen2 == None) :
            m1 = self.__array2DimBedaElemen.copy()
            if(type(array2DimBedaElemen1) == list) : m2 = array2DimBedaElemen1.copy()
            elif(type(array2DimBedaElemen1) == Array2DimBedaElemen) : m2 = array2DimBedaElemen1.__array2DimBedaElemen.copy()
            else : m2 = Array2DimBedaElemen(array2DimBedaElemen1).__array2DimBedaElemen.copy()
        else : 
            m1 = array2DimBedaElemen1.copy() if(type(array2DimBedaElemen1) == list) else array2DimBedaElemen1.__array2DimBedaElemen.copy() if(type(array2DimBedaElemen1) == Array2DimBedaElemen) else Array2DimBedaElemen(array2DimBedaElemen1).__array2DimBedaElemen.copy()
            m2 = array2DimBedaElemen2.copy() if(type(array2DimBedaElemen2) == list) else array2DimBedaElemen2.__array2DimBedaElemen.copy() if(type(array2DimBedaElemen2) == Array2DimBedaElemen) else Array2DimBedaElemen(array2DimBedaElemen2).__array2DimBedaElemen.copy()
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
        
    # Method overloading selisih2Array2DimBedaElemen
    def selisih2Array2DimBedaElemen(self, array2DimBedaElemen1, array2DimBedaElemen2= None) :
        if(array2DimBedaElemen2 == None) :
            m1 = self.__array2DimBedaElemen.copy()
            if(type(array2DimBedaElemen1) == list) : m2 = array2DimBedaElemen1.copy()
            elif(type(array2DimBedaElemen1) == Array2DimBedaElemen) : m2 = array2DimBedaElemen1.__array2DimBedaElemen.copy()
            else : m2 = Array2DimBedaElemen(array2DimBedaElemen1).__array2DimBedaElemen.copy()
        else : 
            m1 = array2DimBedaElemen1.copy() if(type(array2DimBedaElemen1) == list) else array2DimBedaElemen1.__array2DimBedaElemen.copy() if(type(array2DimBedaElemen1) == Array2DimBedaElemen) else Array2DimBedaElemen(array2DimBedaElemen1).__array2DimBedaElemen.copy()
            m2 = array2DimBedaElemen2.copy() if(type(array2DimBedaElemen2) == list) else array2DimBedaElemen2.__array2DimBedaElemen.copy() if(type(array2DimBedaElemen2) == Array2DimBedaElemen) else Array2DimBedaElemen(array2DimBedaElemen2).__array2DimBedaElemen.copy()
        result = []
        for i in range(max(len(m1),len(m2))) : result.append([])
        for i in range(len(result)) : 
            if(i < min(len(m1),len(m2))) :
                for j in range(max(len(m1[i]),len(m2[i]))) : result[i].append(m1[i][j] - m2[i][j]) if(j < min(len(m1[i]),len(m2[i]))) else result[i].append(m1[i][j]) if (len(m1[i]) == max(len(m1[i]),len(m2[i]))) else result[i].append((-1) * m2[i][j])
            else :
                if(len(result) == len(m1)) : 
                    for num in m1[i] : result[i].append(num)
                else :
                    for num in m2[i] : result[i].append((-1) * num)
        return result
    

    # Method tampilArray2DimBedaElemen -> show Array2DimBedaElemen
    def tampilArray2DimBedaElemen(self, array2DimBedaElemen= None) : 
        m = self.__array2DimBedaElemen if(array2DimBedaElemen == None) else array2DimBedaElemen if(type(array2DimBedaElemen) == list) else array2DimBedaElemen.__array2DimBedaElemen if(type(array2DimBedaElemen) == Array2DimBedaElemen) else [[array2DimBedaElemen]]
        for row in range(len(m)) :
            for col in range(len(m[row])) :
                print(m[row][col],end="\t")
            print()

# Test Class

# Create object
operator = Array2DimBedaElemen()
obj1 = Array2DimBedaElemen(i= 3)
obj2 = Array2DimBedaElemen(i= 3, j= [1,2,3])
obj3 = Array2DimBedaElemen(i= 3, j= [1,2,3])
obj4 = Array2DimBedaElemen([[1,2],[3]])
obj5 = Array2DimBedaElemen(i= 4)

# Call method jumlah2Array2DimBedaElemen
print("obj1 =")
obj1.tampilArray2DimBedaElemen()
print("obj2 =")
obj2.tampilArray2DimBedaElemen()
sum1 = obj1.jumlah2Array2DimBedaElemen(array2DimBedaElemen1= obj2)
print("obj1 + obj2 = ")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sum1)
sum2 = operator.jumlah2Array2DimBedaElemen(array2DimBedaElemen1= obj1, array2DimBedaElemen2= obj2)
print(f"obj1 + obj2 =")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sum2)

print("obj2 =")
obj2.tampilArray2DimBedaElemen()
print("obj3 =")
obj3.tampilArray2DimBedaElemen()
sum3 = obj2.jumlah2Array2DimBedaElemen(array2DimBedaElemen1= obj3)
print("obj2 + obj3 = ")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sum3)
sum4 = operator.jumlah2Array2DimBedaElemen(array2DimBedaElemen1= obj2, array2DimBedaElemen2= obj3)
print(f"obj2 + obj3 =")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sum4)

print("obj4 =")
obj4.tampilArray2DimBedaElemen()
print("obj5 =")
obj5.tampilArray2DimBedaElemen()
sum5 = obj4.jumlah2Array2DimBedaElemen(array2DimBedaElemen1= obj5)
print("obj4 + obj5 = ")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sum5)
sum6 = operator.jumlah2Array2DimBedaElemen(array2DimBedaElemen1= obj4, array2DimBedaElemen2= obj5)
print(f"obj4 + obj5 =")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sum6)

# Call method selisih2Array2DimBedaElemen
print("obj1 =")
obj1.tampilArray2DimBedaElemen()
print("obj2 =")
obj2.tampilArray2DimBedaElemen()
sel1 = obj1.selisih2Array2DimBedaElemen(array2DimBedaElemen1= obj2)
print("obj1 - obj2 = ")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sel1)
sel2 = operator.selisih2Array2DimBedaElemen(array2DimBedaElemen1= obj1, array2DimBedaElemen2= obj2)
print(f"obj1 - obj2 =")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sel2)

print("obj2 =")
obj2.tampilArray2DimBedaElemen()
print("obj3 =")
obj3.tampilArray2DimBedaElemen()
sel3 = obj2.selisih2Array2DimBedaElemen(array2DimBedaElemen1= obj3)
print("obj2 - obj3 = ")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sel3)
sel4 = operator.selisih2Array2DimBedaElemen(array2DimBedaElemen1= obj2, array2DimBedaElemen2= obj3)
print(f"obj2 - obj3 =")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sel4)

print("obj4 =")
obj4.tampilArray2DimBedaElemen()
print("obj5 =")
obj5.tampilArray2DimBedaElemen()
sel5 = obj4.selisih2Array2DimBedaElemen(array2DimBedaElemen1= obj5)
print("obj4 - obj5 = ")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sel5)
sel6 = operator.selisih2Array2DimBedaElemen(array2DimBedaElemen1= obj4, array2DimBedaElemen2= obj5)
print(f"obj4 - obj5 =")
operator.tampilArray2DimBedaElemen(array2DimBedaElemen= sel6)