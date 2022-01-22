'''
This code was created by Robanu Dakhayin
'''

# import library math
import math

# Create class BendaBulat
class BendaBulat :

    # Constructor
    def __init__(self) :
        self.__radius = float(1)

    # Method set value of radius
    def setRadius(self,radius) :
        self.__radius = float(radius)

    # Method get value of radius
    def getRadius(self) :
        return self.__radius

    # Method kelilingLingkaran() : float
    def kelilingLingkaran(self) :
        return 2 * math.pi * self.getRadius()

    # Method luasLingkaran() : float
    def luasLingkaran(self) :
        return math.pi * math.pow(self.getRadius(),2)

    # Method volumeBola() : float
    def volumeBola(self) :
        return 4 / 3 * math.pi * math.pow(self.getRadius(),3)


# Test Class

# Create object BendaBulat
print(">> bendaBulat = BendaBulat()")
bendaBulat = BendaBulat()

# Set value of radius
print(">> bendaBulat.setRadius(radius= 10)")
bendaBulat.setRadius(radius= 10)

# Get value of kelilingLingkaran
print(">> kelilingLingkaran = bendaBulat.kelilingLingkaran()")
kelilingLingkaran = bendaBulat.kelilingLingkaran()

# Get value of luasLingkaran
print(">> luasLingkaran = bendaBulat.luasLingkaran()")
luasLingkaran = bendaBulat.luasLingkaran()

# Get value of volumeBola
print(">> volumeBola = bendaBulat.volumeBola()")
volumeBola = bendaBulat.volumeBola()

# Display radius, kelilingLingkaran, luasLingkaran, and volumeBola
print(">> print(f\"Radius = {bendaBulat.getRadius()}\")")
print(f"Radius = {bendaBulat.getRadius()}")

print(">> print(\"Keliling Lingkaran =\",format(kelilingLingkaran,\"0.2f\"))")
print("Keliling Lingkaran =",format(kelilingLingkaran,"0.2f"))

print(">> print(\"Luas Lingkaran =\",format(luasLingkaran,\"0.2f\"))")
print("Luas Lingkaran =",format(luasLingkaran,"0.2f"))

print(">> print(\"Volume Bola =\",format(volumeBola,\"0.2f\"))")
print("Volume Bola =",format(volumeBola,"0.2f"))