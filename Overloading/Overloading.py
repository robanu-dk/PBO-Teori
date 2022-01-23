'''
This code was created by Robanu Dakhayin
'''

# Create class JumlahBilanganBulat
class JumlahBilanganBulat :

    # method Overloading -> sum(a, b, c, d)
    def sum(self, a = None, b = None, c = None, d = None) :
        if(a != None and b != None and c != None and d != None) : return a + b + c + d
        elif(a != None and b != None and c != None): return self.sum(a= a,b= b,c= c,d= 0)
        elif(a != None and b != None) : return self.sum(a= a,b= b,c= 0,d= 0)
        elif(a != None) : return a
        else : return 0


# Create class HitungBungaMajemuk
class HitungBungaMajemuk :
    
    # Method overloading mt(mo,n,r) -> for calculate bunga majemuk
    def mt(self,mo= None, n= None, r= None):
        if (mo != None and n != None and r != None) : return int(mo) * ((1 + (r/100)) ** int(n))
        elif (mo != None and n != None) : return self.mt(mo= mo,n= n,r= 10)
        elif (mo != None) : return self.mt(mo= mo, n= 1, r= 10)
        else : return self.mt(mo= 1000,n= 1,r= 10)


# Create class Silinder
class Silinder :

    # Method overloading volumeSilinder(r,t) -> for calculate volume of silinder
    def volumeSilinder(self,r= None,t= None) :
        if(r != None and t != None) : return 3.14 * (r ** 2) * t
        elif(r != None) : return self.volumeSilinder(r= r,t= 1)
        else : return self.volumeSilinder(r= 1,t= 1)


# Create class Balok
class Balok :

    # Method overloading volumeBalok(p,l,t) -> for calculate volume of balok
    def volumeBalok(self,p= None,l= None,t= None) :
        if(p != None and l != None and t != None) : return p * l * t
        elif(p != None and l != None) : return p * l
        elif(p != None) : return p
        else : return 0


# Test Class

'----------------------------------------------------------------------------------------------------------------------------------------------'

print(">>> print(\"----------------------------------Test Class JumlahBilanganBulat----------------------------------\")")
print("----------------------------------Test Class JumlahBilanganBulat----------------------------------")

# Create object class JumlahBilanganBulat
print(">>> add = JumlahBilanganBulat()")
add = JumlahBilanganBulat()

# Sum four whole numbers
print(">>> print(f\"1 + 2 + 3 + 4 = {add.sum(a= 1,b= 2,c= 3,d= 4)}\")")
print(f"1 + 2 + 3 + 4 = {add.sum(a= 1,b= 2,c= 3,d= 4)}")

# Sum three whole numbers
print(">>> print(f\"1 + 2 + 3 = {add.sum(a= 1,b= 2,c= 3)}\")")
print(f"1 + 2 + 3 = {add.sum(a= 1,b= 2,c= 3)}")

# Sum two whole numbers
print(">>> print(f\"1 + 2 = {add.sum(a= 1,b= 2)}\")")
print(f"1 + 2 = {add.sum(a= 1,b= 2)}")

# Sum one whole numbers
print(">>> print(add.sum(a= 1))")
print(add.sum(a= 1))

# Sum no whole numbers
print(">>> print(add.sum())")
print(add.sum())


'----------------------------------------------------------------------------------------------------------------------------------------------'

print(">>> print(\"-----------------------------------Test Class HitungBungaMajemuk----------------------------------\")")
print("-----------------------------------Test Class HitungBungaMajemuk----------------------------------")

# Create object
print(">>> bungaMajemuk = HitungBungaMajemuk()")
bungaMajemuk = HitungBungaMajemuk()

# Calculate bunga majemuk with 3 param and display it
print(">>> bunga1 = bungaMajemuk.mt(mo= 100000,n= 3,r= 25)")
bunga1 = bungaMajemuk.mt(mo= 100000,n= 3,r= 25)

print(">>> print(f\"Bunga Majemuk = {bunga1}\")")
print(f"Bunga Majemuk = {bunga1}")

# Calculate bunga majemuk with 2 param and display it
print(">>> bunga2 = bungaMajemuk.mt(mo= 100000,n= 3)")
bunga2 = bungaMajemuk.mt(mo= 100000,n= 3)

print(">>> print(f\"Bunga Majemuk = {bunga2}\")")
print(f"Bunga Majemuk = {bunga2}")

# Calculate bunga majemuk with 1 param and display it
print(">>> bunga3 = bungaMajemuk.mt(mo= 100000)")
bunga3 = bungaMajemuk.mt(mo= 100000)

print(">>> print(f\"Bunga Majemuk = {bunga3}\")")
print(f"Bunga Majemuk = {bunga3}")

# Calculate bunga majemuk with no param and display it
print(">>> bunga4 = bungaMajemuk.mt()")
bunga4 = bungaMajemuk.mt()

print(">>> print(f\"Bunga Majemuk = {bunga4}\")")
print(f"Bunga Majemuk = {bunga4}")


'----------------------------------------------------------------------------------------------------------------------------------------------'

print(">>> print(\"----------------------------------------Test Class Silinder---------------------------------------\")")
print("----------------------------------------Test Class Silinder---------------------------------------")

# Create object
print(">>> silinder = Silinder()")
silinder = Silinder()

# Calculate silinder with two param and display it
print(">>> volume1 = silinder.volumeSilinder(r= 10,t= 15)")
volume1 = silinder.volumeSilinder(r= 10,t= 15)

print(">>> print(f\"Volume silinder = {volume1}\")")
print(f"Volume silinder = {volume1}")

# Calculate silinder with one param (radius or r) and display it
print(">>> volume2 = silinder.volumeSilinder(r= 10)")
volume2 = silinder.volumeSilinder(r= 10)

print(">>> print(f\"Volume silinder = {volume2}\")")
print(f"Volume silinder = {volume2}")

# Calculate silinder with no param and display it
print(">>> volume3 = silinder.volumeSilinder()")
volume3 = silinder.volumeSilinder()

print(">>> print(f\"Volume silinder = {volume3}\")")
print(f"Volume silinder = {volume3}")

'----------------------------------------------------------------------------------------------------------------------------------------------'

print(">>> print(\"-----------------------------------------Test Class Balok-----------------------------------------\")")
print("-----------------------------------------Test Class Balok-----------------------------------------")

# Create object
balok = Balok()

# Calculate value of balok with 3 param and display it
print(">>> volume_balok1 = balok.volumeBalok(p= 10,l= 20,t= 2)")
volume_balok1 = balok.volumeBalok(p= 10,l= 20,t= 2)

print(">>> print(f\"Volume balok = {volume_balok1}\")")
print(f"Volume balok = {volume_balok1}")

# Calculate value of balok with 2 param and display it
print(">>> volume_balok1 = balok.volumeBalok(p= 10,l= 20)")
volume_balok2 = balok.volumeBalok(p= 10,l= 20)

print(">>> print(f\"Volume balok = {volume_balok2}\")")
print(f"Volume balok = {volume_balok2}")

# Calculate value of balok with 1 param and display it
print(">>> volume_balok1 = balok.volumeBalok(p= 10)")
volume_balok3 = balok.volumeBalok(p= 10)

print(">>> print(f\"Volume balok = {volume_balok3}\")")
print(f"Volume balok = {volume_balok3}")

# Calculate value of balok with no param and display it
print(">>> volume_balok1 = balok.volumeBalok()")
volume_balok4 = balok.volumeBalok()

print(">>> print(f\"Volume balok = {volume_balok4}\")")
print(f"Volume balok = {volume_balok4}")