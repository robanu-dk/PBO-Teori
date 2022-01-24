'''
This code was created by Robanu Dakhayin
'''


class Vektor :

    # Constructor
    def __init__(self, v= None) :
        if(v!= None) :
            self.__v = v if(type(v) == list) else [v]
        else :
            self.__v = []

    # Method overloading jumlah2Vektor() : Vektor
    def jumlah2Vektor(self, v1, v2= None) :
        if(v2!= None) :
            a = v1.__v.copy()
            b = v2.__v.copy()
        else :
            a = self.__v.copy()
            b = v1.__v.copy()
        result = []
        for i in range(max(len(a), len(b))) : 
            if(i < min(len(a), len(b))) : result.append(a[i] + b[i])
            else : result.append(a[i]) if(len(a) > len(b)) else result.append(b[i])
        return Vektor(v= result)

    # Method overloading selisih2Vektor() : Vektor
    def selisih2Vektor(self, v1, v2= None) :
        if(v2!= None) :
            a = v1.__v.copy()
            b = v2.__v.copy()
        else :
            a = self.__v.copy()
            b = v1.__v.copy()
        result = []
        for i in range(max(len(a), len(b))) : 
            if(i < min(len(a), len(b))) : result.append(a[i] + b[i])
            else : result.append(a[i]) if(len(a) > len(b)) else result.append(((-1) * b[i]))
        return Vektor(v= result)

    # Method tampilVektor(Vektor v) -> menampilkan vektor
    def tampilVektor(self,v) :
        print("[",end="")
        for i in range(len(v.__v)) :
            print(v.__v[i],end= ", " if(i != len(v.__v) - 1) else "")
        print("]")


# Test class

# Create object
print(">>> op = Vektor()")
op = Vektor()

print(">>> v1 = Vektor(v= [1, 2, 3])")
v1 = Vektor(v= [1, 2, 3])

print(">>> v2 = Vektor(v= 1)")
v2 = Vektor(v= 1)

print(">>> v3 = Vektor(v= [4, 5, 6])")
v3 = Vektor(v= [4, 5, 6])

print(">>> v4 = Vektor(v= [1, 2, 3, 4, 5, 6])")
v4 = Vektor(v= [1, 2, 3, 4, 5, 6])

# Call method jumlah2Vektor()
print(">>> sum1 = op.jumlah2Vektor(v1= v1, v2= v2)")
sum1 = op.jumlah2Vektor(v1= v1, v2= v2)

print(">>> sum2 = op.jumlah2Vektor(v1= v1, v2= v3)")
sum2 = op.jumlah2Vektor(v1= v1, v2= v3)

print(">>> sum3 = op.jumlah2Vektor(v1= v1, v2= v4)")
sum3 = op.jumlah2Vektor(v1= v1, v2= v4)

print(">>> sum4 = v1.jumlah2Vektor(v1= v2)")
sum4 = v1.jumlah2Vektor(v1= v2)

print(">>> sum5 = v1.jumlah2Vektor(v1= v3)")
sum5 = v1.jumlah2Vektor(v1= v3)

print(">>> sum6 = v1.jumlah2Vektor(v1= v4)")
sum6 = v1.jumlah2Vektor(v1= v4)

# Call method selisih2Vektor()
print(">>> selisih1 = op.selisih2Vektor(v1= v1, v2= v2)")
selisih1 = op.selisih2Vektor(v1= v1, v2= v2)

print(">>> selisih2 = op.selisih2Vektor(v1= v1, v2= v3)")
selisih2 = op.selisih2Vektor(v1= v1, v2= v3)

print(">>> selisih3 = op.selisih2Vektor(v1= v1, v2= v4)")
selisih3 = op.selisih2Vektor(v1= v1, v2= v4)

print(">>> selisih4 = v1.selisih2Vektor(v1= v2)")
selisih4 = v1.selisih2Vektor(v1= v2)

print(">>> selisih5 = v1.selisih2Vektor(v1= v3)")
selisih5 = v1.selisih2Vektor(v1= v3)

print(">>> selisih6 = v1.selisih2Vektor(v1= v4)")
selisih6 = v1.selisih2Vektor(v1= v4)

print(">>> selisih7 = v4.selisih2Vektor(v1= v1)")
selisih7 = v4.selisih2Vektor(v1= v1)

# Call method tampilVektor()
print(">>> op.tampilVektor(v= sum1)")
op.tampilVektor(v= sum1)

print(">>> op.tampilVektor(v= sum2)")
op.tampilVektor(v= sum2)

print(">>> op.tampilVektor(v= sum3)")
op.tampilVektor(v= sum3)

print(">>> op.tampilVektor(v= sum4)")
op.tampilVektor(v= sum4)

print(">>> op.tampilVektor(v= sum5)")
op.tampilVektor(v= sum5)

print(">>> op.tampilVektor(v= sum6)")
op.tampilVektor(v= sum6)

print(">>> op.tampilVektor(v= selisih1)")
op.tampilVektor(v= selisih1)

print(">>> op.tampilVektor(v= selisih2)")
op.tampilVektor(v= selisih2)

print(">>> op.tampilVektor(v= selisih3)")
op.tampilVektor(v= selisih3)

print(">>> op.tampilVektor(v= selisih4)")
op.tampilVektor(v= selisih4)

print(">>> op.tampilVektor(v= selisih5)")
op.tampilVektor(v= selisih5)

print(">>> op.tampilVektor(v= selisih6)")
op.tampilVektor(v= selisih6)

print(">>> op.tampilVektor(v= selisih7)")
op.tampilVektor(v= selisih7)