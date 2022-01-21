'''
This code was created by Robanu Dakhayin
'''


# import library math
import math

# Class BendaBulat
class BendaBulat:

    # Constructor
    def __init__(self) :
        self.__radius = 1
        self.__luas_lingkaran = None
        self.__volume_bola = None

    # Set Radius
    def setRadius(self, radius) :
        self.__radius = radius

    # Method luasLingkaran()
    def luasLingkaran(self) :
        self.__luas_lingkaran = math.pi * math.pow(self.__radius,2)
    
    # Method getLuasLingkaran() : float -> return circle's area
    def getLuasLingkaran(self) :
        self.luasLingkaran()
        return self.__luas_lingkaran

    # Method volumeBola() :
    def volumeBola(self) :
        self.__volume_bola = 4 / 3 * math.pi * math.pow(self.__radius,3)

    # Method getVolumeBola() : float -> return bola's volume
    def getVolumeBola(self) :
        self.volumeBola()
        return self.__volume_bola

# Test class BendaBulat

# Create object BendaBulat
print(">> bendaBulat = BendaBulat()")
bendaBulat = BendaBulat()

# Input radius value
print(">> radius = float(input(\"Radius = \"))")
radius = float(input("Radius= "))

# Call method setRadius() for set radius value
print(">> bendaBulat.setRadius(radius= radius)")
bendaBulat.setRadius(radius= radius)

# Call method getLuasLingkaran() to get circle's area
print(">> area = bendaBulat.getLuasLingkaran()")
area = bendaBulat.getLuasLingkaran()

# Call method getVolumeBola() to get bola's volume
print(">> volume = bendaBulat.getVolumeBola()")
volume = bendaBulat.getVolumeBola()

# Display radius, area, and volume
print(">> print(f\"Radius= {radius}\")")
print(f"Radius= {radius}")

print(">> print(\"Area= \",format(area,\"0.2f\"))")
print("Area= ",format(area,"0.2f"))

print(">> print(\"Volume= \",format(volume,\"0.2f\"))")
print("Volume= ",format(volume,"0.2f"))
