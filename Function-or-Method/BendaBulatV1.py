'''
This code was created by Robanu Dakhayin
'''


# import library math
import math

# Class BendaBulat
class BendaBulat:

    # Method luasLingkaran(radius : float) : float -> return circle's area
    def luasLingkaran(self,radius) :
        return math.pi * math.pow(radius,2)
    
    # Method volumeBola(radius : float) : float -> return bola's volume
    def volumeBola(self,radius) :
        return 4 / 3 * math.pi * math.pow(radius,3)

# Test class BendaBulat

# Create object BendaBulat
print(">> bendaBulat = BendaBulat()")
bendaBulat = BendaBulat()

# Input radius value
print(">> radius = float(input(\"Radius = \"))")
radius = float(input("Radius= "))

# Call method luasLingkaran(radius)
print(">> area = bendaBulat.luasLingkaran(radius= radius)")
area = bendaBulat.luasLingkaran(radius= radius)

# Call method volumeBola(radius= radius)
print(">> volume = bendaBulat.volumeBola(radius= radius)")
volume = bendaBulat.volumeBola(radius= radius)

# Display radius, area, and volume
print(">> print(f\"Radius= {radius}\")")
print(f"Radius= {radius}")

print(">> print(\"Area= \",format(area,\"0.2f\"))")
print("Area= ",format(area,"0.2f"))

print(">> print(\"Volume= \",format(volume,\"0.2f\"))")
print("Volume= ",format(volume,"0.2f"))
