'''
This code created by Robanu Dakhayin
'''

# import library math
import math

# Create class BidangSegi4
class BidangSegi4 :

    # Method luasBujurSangkar(panjang : float) : float -> return Bujur Sangkar area
    def luasBujurSangkar(self, panjang) :
        return math.pow(panjang, 2)

    # Method luasPersegiPanjang(panjang : float, lebar : float) : float -> return area of rectangle
    def luasPersegiPanjang(self, panjang, lebar) :
        return panjang * lebar


# Test Class

# Create object BidangSegi4
print(">> benda = BidangSegi4()")
benda = BidangSegi4()

# Call method luasBujurSangkar(panjang)
print(">> luasBujurSangkar = benda.luasBujurSangkar(panjang= 10)")
luasBujurSangkar = benda.luasBujurSangkar(panjang= 10)

#  Display luasBujurSangkar
print(">> print(f\"Luas Bujur Sangkar= {luasBujurSangkar}\")")
print(f"Luas Bujur Sangkar= {luasBujurSangkar}")

# Call method luasPersegiPanjang(panjang, lebar)
print(">> luasPersegiPanjang = benda.luasPersegiPanjang(panjang= 10, lebar= 8)")
luasPersegiPanjang = benda.luasPersegiPanjang(panjang= 10, lebar= 8)

# Display luasPersegiPanjang
print(">> print(f\"Luas Persegi Panjang = {luasPersegiPanjang}\")")
print(f"Luas Persegi Panjang = {luasPersegiPanjang}")