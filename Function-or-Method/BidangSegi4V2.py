'''
This code created by Robanu Dakhayin
'''

# import library math
import math

# Create class BidangSegi4
class BidangSegi4 :

    # Constructor
    def __init__(self) :
        self.__panjang = 1
        self.__lebar = 1
        self.__luas_bujur_sangkar = None
        self.__luas_persegi_panjang = None

    # Method setter
    def setPanjang(self, panjang) : self.__panjang = panjang

    def setLebar(self, lebar) : self.__lebar = lebar

    # Method luasBujurSangkar()
    def luasBujurSangkar(self) :
        self.__luas_bujur_sangkar = math.pow(self.__panjang, 2)

    # Method luasPersegiPanjang()
    def luasPersegiPanjang(self) :
        self.__luas_persegi_panjang = self.__panjang * self.__lebar

    # Method getLuasBujurSangkar() -> return value of Bujur Sangkar's area
    def getLuasBujurSangkar(self) :
        self.luasBujurSangkar()
        return self.__luas_bujur_sangkar
    
    # Method getLuasPersegiPanjang() -> return value of Persegi Panjang's area
    def getLuasPersegiPanjang(self) :
        self.luasPersegiPanjang()
        return self.__luas_persegi_panjang

# Test Class

# Create object BidangSegi4
print(">> benda = BidangSegi4()")
benda = BidangSegi4()

# Set panjang
print(">> benda.setPanjang(panjang= 10)")
benda.setPanjang(panjang= 10)

# Set lebar
print(">> benda.setLebar(lebar= 8)")
benda.setLebar(lebar= 8)

# Call method getLuasBujurSangkar() to get value of Bujur Sangkar's area
print(">> luasBujurSangkar = benda.getLuasBujurSangkar()")
luasBujurSangkar = benda.getLuasBujurSangkar()

#  Display luasBujurSangkar
print(">> print(f\"Luas Bujur Sangkar= {luasBujurSangkar}\")")
print(f"Luas Bujur Sangkar= {luasBujurSangkar}")

# Call method getLuasPersegiPanjang() to get value of Persegi Panjang's area
print(">> luasPersegiPanjang = benda.getLuasPersegiPanjang()")
luasPersegiPanjang = benda.getLuasPersegiPanjang()

# Display luasPersegiPanjang
print(">> print(f\"Luas Persegi Panjang = {luasPersegiPanjang}\")")
print(f"Luas Persegi Panjang = {luasPersegiPanjang}")