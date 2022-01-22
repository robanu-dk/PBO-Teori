'''
This code was created by Robanu Dakhayin
'''


# Create class
class BendaSegi4 :

    # Constructor
    def __init__(self) :
        self.__panjang = float(1)
        self.__lebar = float(1)
        self.__panjangSisiBujurSangkar = float(1)

    # Method setPanjang(panjang : float)
    def setPanjang(self, panjang) : self.__panjang = float(panjang)

    # Method setLebar(lebar : float)
    def setLebar(self, lebar) : self.__lebar = float(lebar)

    # Method setPanjangSisiBujurSangkar(panjangSisiBujurSangkar : float)
    def setPanjangSisiBujurSangkar(self, panjangSisiBujurSangkar) : self.__panjangSisiBujurSangkar = float(panjangSisiBujurSangkar)

    # Method getPanjang() : float
    def getPanjang(self) : return self.__panjang

    # Method getLebar() : float
    def getLebar(self) : return self.__lebar

    # Method getPanjangSisiBujurSangkar() : float
    def getPanjangSisiBujurSangkar(self) : return self.__panjangSisiBujurSangkar

    # Method kelilingBujurSangkar() : float
    def kelilingBujurSangkar(self) : return 4 * self.getPanjangSisiBujurSangkar()

    # Method kelilingPersegiPanjang() : float
    def kelilingPersegiPanjang(self) : return 2 * (self.getLebar() + self.getPanjang())

    # Method luasBujurSangkar() : float
    def luasBujurSangkar(self) : return self.getPanjangSisiBujurSangkar() * self.getPanjangSisiBujurSangkar()

    # Method luasPersegiPanjang() : float
    def luasPersegiPanjang(self) : return self.getPanjang() * self.getLebar()



# Test Class

# Create object BendaSegi4
print(">> benda = BendaSegi4()")
benda = BendaSegi4()

# Set panjang, lebar, and panjangSisiBujurSangkar
print(">> benda.setPanjang(panjang= 10)")
benda.setPanjang(panjang= 10)

print(">> benda.setLebar(lebar= 8)")
benda.setLebar(lebar= 8)

print(">> benda.setPanjangSisiBujurSangkar(panjangSisiBujurSangkar= 6)")
benda.setPanjangSisiBujurSangkar(panjangSisiBujurSangkar= 6)

# Search value of kelilingBujurSangkar, kelilingPersegiPanjang, luasBujurSangkar, and luasPersegiPanjang
print(">> kelilingBujurSangkar = benda.kelilingBujurSangkar()")
kelilingBujurSangkar = benda.kelilingBujurSangkar()

print(">> kelilingPersegiPanjang = benda.kelilingPersegiPanjang()")
kelilingPersegiPanjang = benda.kelilingPersegiPanjang()

print(">> luasBujurSangkar = benda.luasBujurSangkar()")
luasBujurSangkar = benda.luasBujurSangkar()

print(">> luasPersegiPanjang = benda.luasPersegiPanjang()")
luasPersegiPanjang = benda.luasPersegiPanjang()

# Display panjang, lebar, panjangSisiBujurSangkar, kelilingBujurSangkar, kelilingPersegiPanjang, luasBujurSangkar, and luasPersegiPanjang
print(">> print(f\"Panjang = {benda.getPanjang()}\")")
print(f"Panjang = {benda.getPanjang()}")

print(">> print(f\"Lebar = {benda.getLebar()}\")")
print(f"Lebar = {benda.getLebar()}")

print(">> print(f\"Panjang Sisi Bujur Sangkar = {benda.getPanjangSisiBujurSangkar()}\")")
print(f"Panjang Sisi Bujur Sangkar = {benda.getPanjangSisiBujurSangkar()}")

print(">> print(f\"Keliling Bujur Sangkar = {kelilingBujurSangkar}\")")
print(f"Keliling Bujur Sangkar = {kelilingBujurSangkar}")

print(">> print(f\"Keliling Persegi Panjang = {kelilingPersegiPanjang}\")")
print(f"Keliling Persegi Panjang = {kelilingPersegiPanjang}")

print(">> print(f\"Luas Bujur Sangkar = {luasBujurSangkar}\")")
print(f"Luas Bujur Sangkar = {luasBujurSangkar}")

print(">> print(f\"Luas Persegi Panjang = {luasPersegiPanjang}\")")
print(f"Luas Persegi Panjang = {luasPersegiPanjang}")