'''
This code was created by Robanu Dakhayin
'''

# Import library
from random import randint

class Array3DimSama :

    # Constructor
    def __init__(self, i= None, j= None, k= None) :
        if(type(i) == list) : self.__array3DimSama = i
        elif(i != None and j != None and k != None) :
            self.__array3DimSama = []
            for l in range(i) : self.__array3DimSama.append([])
            for l in range(i) : 
                for m in range(j) : self.__array3DimSama[l].append([])
            for l in range(i) : 
                for m in range(j) :
                    for n in range(k) : self.__array3DimSama[l][m].append(randint(a= 0, b= 100))
        elif(i != None and j != None) : self.__init__(i= i, j= j, k= randint(a= 1, b= 5))
        elif(i != None and k != None) : self.__init__(i= i, j= randint(a= 1, b= 5), k= k)
        elif(j != None and k != None) : self.__init__(i= randint(a= 1, b= 5), j= j, k= k)
        elif(i != None) : self.__init__(i= i, j= randint(a= 1, b= 5), k= randint(a= 1, b= 5))
        elif(j != None) : self.__init__(i= randint(a= 1, b= 5), j= j, k= randint(a= 1, b= 5))
        elif(k != None) : self.__init__(i= randint(a= 1, b= 5), j= randint(a= 1, b= 5), k= k)
        else : self.__init__(i= randint(a= 1, b= 5), j= randint(a= 1, b= 5), k= randint(a= 1, b= 5))

    # Method jumlah2Array3DimSama -> sum Array3DimSama
    def jumlah2Array3DimSama(self, array3DimSama1, array3DimSama2= None) :
        if(array3DimSama2 == None) :
            m1 = self.__array3DimSama.copy()
            if(type(array3DimSama1) == list) : m2 = array3DimSama1.copy()
            elif(type(array3DimSama1) == Array3DimSama) : m2 = array3DimSama1.__array3DimSama.copy()
            else : m2 = Array3DimSama(array3DimSama1).__array3DimSama.copy()
        else : 
            m1 = array3DimSama1.copy() if(type(array3DimSama1) == list) else array3DimSama1.__array3DimSama.copy() if(type(array3DimSama1) == Array3DimSama) else Array3DimSama(array3DimSama1).__array3DimSama.copy()
            m2 = array3DimSama2.copy() if(type(array3DimSama2) == list) else array3DimSama2.__array3DimSama.copy() if(type(array3DimSama2) == Array3DimSama) else Array3DimSama(array3DimSama2).__array3DimSama.copy()
        result = []
        for i in range(max(len(m1),len(m2))) : result.append([])
        for i in range(max(len(m1),len(m2))) :
            if(i < min(len(m1),len(m2))) :
                for _ in range(max(len(m1[i]),len(m2[i]))) :
                    result[i].append([])
            else :
                if(len(result) == len(m1)) :
                    for _ in range(len(m1[i])) :
                        result[i].append([])
                else :
                    for _ in range(len(m2[i])) :
                        result[i].append([])
        for i in range(len(result)) : 
            if(i < min(len(m1),len(m2))) :
                for j in range(max(len(m1[i]),len(m2[i]))) : 
                    if(j < min(len(m1[i]),len(m2[i]))) :
                        for k in range(max(len(m1[i][j]),len(m2[i][j]))) : 
                            result[i][j].append(m1[i][j][k] + m2[i][j][k]) if(k < min(len(m1[i][j]),len(m2[i][j]))) else result[i][j].append(m1[i][j][k]) if (len(m1[i][j]) == max(len(m1[i][j]),len(m2[i][j]))) else result[i][j].append(m2[i][j][k])
                    else :
                        if(len(m1[i]) == max(len(m1[i]),len(m2[i]))) :
                            for num in m1[i][j] : result[i][j].append(num)
                        else :
                            for num in m2[i][j] : result[i][j].append(num)
            else :
                if(len(result) == len(m1)) : 
                    for num in m1[i] : result[i].append(num)
                else :
                    for num in m2[i] : result[i].append(num)
        return result
        
    # Method overloading selisih2Array3DimSama
    def selisih2Array3DimSama(self, array3DimSama1, array3DimSama2= None) :
        if(array3DimSama2 == None) :
            m1 = self.__array3DimSama.copy()
            if(type(array3DimSama1) == list) : m2 = array3DimSama1.copy()
            elif(type(array3DimSama1) == Array3DimSama) : m2 = array3DimSama1.__array3DimSama.copy()
            else : m2 = Array3DimSama(array3DimSama1).__array3DimSama.copy()
        else : 
            m1 = array3DimSama1.copy() if(type(array3DimSama1) == list) else array3DimSama1.__array3DimSama.copy() if(type(array3DimSama1) == Array3DimSama) else Array3DimSama(array3DimSama1).__array3DimSama.copy()
            m2 = array3DimSama2.copy() if(type(array3DimSama2) == list) else array3DimSama2.__array3DimSama.copy() if(type(array3DimSama2) == Array3DimSama) else Array3DimSama(array3DimSama2).__array3DimSama.copy()
        result = []
        for i in range(max(len(m1),len(m2))) : result.append([])
        for i in range(max(len(m1),len(m2))) :
            if(i < min(len(m1),len(m2))) :
                for _ in range(max(len(m1[i]),len(m2[i]))) :
                    result[i].append([])
            else :
                if(len(result) == len(m1)) :
                    for _ in range(len(m1[i])) :
                        result[i].append([])
                else :
                    for _ in range(len(m2[i])) :
                        result[i].append([])
        for i in range(len(result)) : 
            if(i < min(len(m1),len(m2))) :
                for j in range(max(len(m1[i]),len(m2[i]))) : 
                    if(j < min(len(m1[i]),len(m2[i]))) :
                        for k in range(max(len(m1[i][j]),len(m2[i][j]))) : 
                            result[i][j].append(m1[i][j][k] - m2[i][j][k]) if(k < min(len(m1[i][j]),len(m2[i][j]))) else result[i][j].append(m1[i][j][k]) if (len(m1[i][j]) == max(len(m1[i][j]),len(m2[i][j]))) else result[i][j].append((-1) * m2[i][j][k])
                    else :
                        if(len(m1[i]) == max(len(m1[i]),len(m2[i]))) :
                            for num in m1[i][j] : result[i][j].append(num)
                        else :
                            for num in m2[i][j] : result[i][j].append((-1) * num)
            else :
                if(len(result) == len(m1)) : 
                    for num in m1[i] : result[i].append(num)
                else :
                    for j in range(len(m2[i])) :
                        for k in range(len(m2[i][j])) :
                            m2[i][j][k] *= (-1)
                    for num in m2[i] : result[i].append(num)
        return result

    # Method tampilArray3DimSama -> show Array3DimSama
    def tampilArray3DimSama(self, array3DimSama= None) : 
        m = self.__array3DimSama if(array3DimSama == None) else array3DimSama if(type(array3DimSama) == list) else array3DimSama.__array3DimSama if(type(array3DimSama) == Array3DimSama) else [[array3DimSama]]
        for i in range(len(m)) :
            for j in range(len(m[i])) :
                for k in range(len(m[i][j])) :
                    print(m[i][j][k],end="\t")
                print()
            print()


# Test Class

# Create object
operator = Array3DimSama()
obj1 = Array3DimSama(i= 3)
obj2 = Array3DimSama(i= 3, j= 2, k= 3)
obj3 = Array3DimSama(i= 3, j= 2, k= 3)
obj4 = Array3DimSama(j= 2)
obj5 = Array3DimSama(k= 3)

# Call method jumlah2Array3DimSama
print("obj1 =")
obj1.tampilArray3DimSama()
print("obj2 =")
obj2.tampilArray3DimSama()
sum1 = obj1.jumlah2Array3DimSama(array3DimSama1= obj2)
print("obj1 + obj2 = ")
operator.tampilArray3DimSama(array3DimSama= sum1)
sum2 = operator.jumlah2Array3DimSama(array3DimSama1= obj1, array3DimSama2= obj2)
print(f"obj1 + obj2 =")
operator.tampilArray3DimSama(array3DimSama= sum2)

print("obj2 =")
obj2.tampilArray3DimSama()
print("obj3 =")
obj3.tampilArray3DimSama()
sum3 = obj2.jumlah2Array3DimSama(array3DimSama1= obj3)
print("obj2 + obj3 = ")
operator.tampilArray3DimSama(array3DimSama= sum3)
sum4 = operator.jumlah2Array3DimSama(array3DimSama1= obj2, array3DimSama2= obj3)
print(f"obj2 + obj3 =")
operator.tampilArray3DimSama(array3DimSama= sum4)

print("obj4 =")
obj4.tampilArray3DimSama()
print("obj5 =")
obj5.tampilArray3DimSama()
sum5 = obj4.jumlah2Array3DimSama(array3DimSama1= obj5)
print("obj4 + obj5 = ")
operator.tampilArray3DimSama(array3DimSama= sum5)
sum6 = operator.jumlah2Array3DimSama(array3DimSama1= obj4, array3DimSama2= obj5)
print(f"obj4 + obj5 =")
operator.tampilArray3DimSama(array3DimSama= sum6)

# Call method selisih2Array3DimSama
print("obj1 =")
obj1.tampilArray3DimSama()
print("obj2 =")
obj2.tampilArray3DimSama()
sel1 = obj1.selisih2Array3DimSama(array3DimSama1= obj2)
print("obj1 - obj2 = ")
operator.tampilArray3DimSama(array3DimSama= sel1)
sel2 = operator.selisih2Array3DimSama(array3DimSama1= obj1, array3DimSama2= obj2)
print(f"obj1 - obj2 =")
operator.tampilArray3DimSama(array3DimSama= sel2)

print("obj2 =")
obj2.tampilArray3DimSama()
print("obj3 =")
obj3.tampilArray3DimSama()
sel3 = obj2.selisih2Array3DimSama(array3DimSama1= obj3)
print("obj2 - obj3 = ")
operator.tampilArray3DimSama(array3DimSama= sel3)
sel4 = operator.selisih2Array3DimSama(array3DimSama1= obj2, array3DimSama2= obj3)
print(f"obj2 - obj3 =")
operator.tampilArray3DimSama(array3DimSama= sel4)

print("obj4 =")
obj4.tampilArray3DimSama()
print("obj5 =")
obj5.tampilArray3DimSama()
sel5 = obj4.selisih2Array3DimSama(array3DimSama1= obj5)
print("obj4 - obj5 = ")
operator.tampilArray3DimSama(array3DimSama= sel5)
sel6 = operator.selisih2Array3DimSama(array3DimSama1= obj4, array3DimSama2= obj5)
print(f"obj4 - obj5 =")
operator.tampilArray3DimSama(array3DimSama= sel6)