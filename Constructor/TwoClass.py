'''
This code was created by Robanu Dakhayin
'''


class BendaBulat :

    # Constructor
    def __init__(self, radius= None, tinggi= None) :
        if(radius!= None and tinggi!= None) :
            self.__radius = radius
            self.__tinggi = tinggi
        elif(radius!= None) :self.__init__(radius= radius, tinggi= 1)
        elif(tinggi!= None) :self.__init__(radius= 1, tinggi= tinggi)
        else :self.__init__(radius= 1, tinggi= 1)

    # Method luas lingkaran() : float
    def luasLingkaran(self) :
        return 3.14 * (self.__radius **2)

    # Method volumeBola() : float
    def volumeBola(self) :
        return 4/3 * 3.14 * (self.__radius **3)

    # Method luasPermukaanTabung() : float
    def luasPermukaanTabung(self) :
        return 2 * 3.14 * self.__radius * (self.__tinggi + self.__radius)

    # Method volumeSilinder() : float
    def volumeSilinder(self) :
        return 3.14 * (self.__radius **2) * self.__tinggi


class BendaSegi4 :

    # Constructor
    def __init__(self, panjang= None, lebar= None, tinggi= None) :
        if(panjang!= None and lebar!= None and tinggi!= None) :
            self.__panjang = panjang
            self.__lebar = lebar
            self.__tinggi = tinggi
        elif(panjang!= None and lebar!= None) : self.__init__(panjang= panjang, lebar= lebar, tinggi= 1)
        elif(panjang!= None and tinggi!= None) : self.__init__(panjang= panjang, lebar= 1, tinggi= tinggi)
        elif(lebar!= None and tinggi!= None) : self.__init__(panjang= 1, lebar= lebar, tinggi= tinggi)
        elif(panjang!= None) : self.__init__(panjang= panjang, lebar= 1, tinggi= 1)
        elif(lebar!= None) : self.__init__(panjang= 1, lebar= lebar, tinggi= 1)
        elif(tinggi!= None) : self.__init__(panjang= 1, lebar= 1, tinggi= tinggi)
        else : self.__init__(panjang= 1, lebar= 1, tinggi= 1)

    # Method luasBujurSangkar() : float
    def luasBujurSangkar(self) :
        return self.__panjang **2

    # Method volumeKubus() : float
    def volumeKubus(self) :
        return self.__panjang **3

    # Method luasPersegiPanjang() : float
    def luasPersegiPanjang(self) :
        return self.__panjang * self.__lebar

    # Method volumeBalok() : float
    def volumeBalok(self) :
        return self.__panjang * self.__lebar * self.__tinggi



# Test class

# Create object
print(">>> bendaBulat1 = BendaBulat(radius= 10, tinggi= 20)")
bendaBulat1 = BendaBulat(radius= 10, tinggi= 20)

print(">>> bendaBulat2 = BendaBulat(radius= 10)")
bendaBulat2 = BendaBulat(radius= 10)

print(">>> bendaBulat3 = BendaBulat(tinggi= 20)")
bendaBulat3 = BendaBulat(tinggi= 20)

print(">>> bendaBulat4 = BendaBulat()")
bendaBulat4 = BendaBulat()

print(">>> bendaSegi4_1 = BendaSegi4(panjang= 10, lebar= 8, tinggi= 6)")
bendaSegi4_1 = BendaSegi4(panjang= 10, lebar= 8, tinggi= 6)

print(">>> bendaSegi4_2 = BendaSegi4(panjang= 10, lebar= 8)")
bendaSegi4_2 = BendaSegi4(panjang= 10, lebar= 8)

print(">>> bendaSegi4_3 = BendaSegi4(panjang= 10, tinggi= 6)")
bendaSegi4_3 = BendaSegi4(panjang= 10, tinggi= 6)

print(">>> bendaSegi4_4 = BendaSegi4(lebar= 8, tinggi= 6)")
bendaSegi4_4 = BendaSegi4(lebar= 8, tinggi= 6)

print(">>> bendaSegi4_5 = BendaSegi4(panjang= 10)")
bendaSegi4_5 = BendaSegi4(panjang= 10)

print(">>> bendaSegi4_6 = BendaSegi4(lebar= 8)")
bendaSegi4_6 = BendaSegi4(lebar= 8)

print(">>> bendaSegi4_7 = BendaSegi4(tinggi= 6)")
bendaSegi4_7 = BendaSegi4(tinggi= 6)

print(">>> bendaSegi4_8 = BendaSegi4()")
bendaSegi4_8 = BendaSegi4()

# Display area of circle
print(">>> print(f\"Luas lingkaran bendaBulat1 =  {bendaBulat1.luasLingkaran()}\")")
print(f"Luas lingkaran bendaBulat1 =  {bendaBulat1.luasLingkaran()}")

print(">>> print(f\"Luas lingkaran bendaBulat2 =  {bendaBulat2.luasLingkaran()}\")")
print(f"Luas lingkaran bendaBulat2 =  {bendaBulat2.luasLingkaran()}")

print(">>> print(f\"Luas lingkaran bendaBulat3 =  {bendaBulat3.luasLingkaran()}\")")
print(f"Luas lingkaran bendaBulat3 =  {bendaBulat3.luasLingkaran()}")

print(">>> print(f\"Luas lingkaran bendaBulat4 =  {bendaBulat4.luasLingkaran()}\")")
print(f"Luas lingkaran bendaBulat4 =  {bendaBulat4.luasLingkaran()}")

# Display volume of Bola
print(">>> print(f\"Volume Bola bendaBulat1 = {bendaBulat1.volumeBola()}\")")
print(f"Volume Bola bendaBulat1 = {bendaBulat1.volumeBola()}")

print(">>> print(f\"Volume Bola bendaBulat2 = {bendaBulat2.volumeBola()}\")")
print(f"Volume Bola bendaBulat2 = {bendaBulat2.volumeBola()}")

print(">>> print(f\"Volume Bola bendaBulat3 = {bendaBulat3.volumeBola()}\")")
print(f"Volume Bola bendaBulat3 = {bendaBulat3.volumeBola()}")

print(">>> print(f\"Volume Bola bendaBulat4 = {bendaBulat4.volumeBola()}\")")
print(f"Volume Bola bendaBulat4 = {bendaBulat4.volumeBola()}")

# Display luasPermukaanTabung
print(">>> print(f\"Luas Permukaan Tabung bendaBulat1 = {bendaBulat1.luasPermukaanTabung()}\")")
print(f"Luas Permukaan Tabung bendaBulat1 = {bendaBulat1.luasPermukaanTabung()}")

print(">>> print(f\"Luas Permukaan Tabung bendaBulat2 = {bendaBulat2.luasPermukaanTabung()}\")")
print(f"Luas Permukaan Tabung bendaBulat2 = {bendaBulat2.luasPermukaanTabung()}")

print(">>> print(f\"Luas Permukaan Tabung bendaBulat3 = {bendaBulat3.luasPermukaanTabung()}\")")
print(f"Luas Permukaan Tabung bendaBulat3 = {bendaBulat3.luasPermukaanTabung()}")

print(">>> print(f\"Luas Permukaan Tabung bendaBulat4 = {bendaBulat4.luasPermukaanTabung()}\")")
print(f"Luas Permukaan Tabung bendaBulat4 = {bendaBulat4.luasPermukaanTabung()}")

# Display volume of silinder
print(">>> print(f\"Volume Silinder bendaBulat1 = {bendaBulat1.volumeSilinder()}\")")
print(f"Volume Silinder bendaBulat1 = {bendaBulat1.volumeSilinder()}")

print(">>> print(f\"Volume Silinder bendaBulat2 = {bendaBulat2.volumeSilinder()}\")")
print(f"Volume Silinder bendaBulat2 = {bendaBulat2.volumeSilinder()}")

print(">>> print(f\"Volume Silinder bendaBulat3 = {bendaBulat3.volumeSilinder()}\")")
print(f"Volume Silinder bendaBulat3 = {bendaBulat3.volumeSilinder()}")

print(">>> print(f\"Volume Silinder bendaBulat4 = {bendaBulat4.volumeSilinder()}\")")
print(f"Volume Silinder bendaBulat4 = {bendaBulat4.volumeSilinder()}")

# Display area of bujur sangkar
print(">>> print(f\"Luas Bujur Sangkar bendaSegi4_1 = {bendaSegi4_1.luasBujurSangkar()}\")")
print(f"Luas Bujur Sangkar bendaSegi4_1 = {bendaSegi4_1.luasBujurSangkar()}")

print(">>> print(f\"Luas Bujur Sangkar bendaSegi4_2 = {bendaSegi4_2.luasBujurSangkar()}\")")
print(f"Luas Bujur Sangkar bendaSegi4_2 = {bendaSegi4_2.luasBujurSangkar()}")

print(">>> print(f\"Luas Bujur Sangkar bendaSegi4_3 = {bendaSegi4_3.luasBujurSangkar()}\")")
print(f"Luas Bujur Sangkar bendaSegi4_3 = {bendaSegi4_3.luasBujurSangkar()}")

print(">>> print(f\"Luas Bujur Sangkar bendaSegi4_4 = {bendaSegi4_4.luasBujurSangkar()}\")")
print(f"Luas Bujur Sangkar bendaSegi4_4 = {bendaSegi4_4.luasBujurSangkar()}")

print(">>> print(f\"Luas Bujur Sangkar bendaSegi4_5 = {bendaSegi4_5.luasBujurSangkar()}\")")
print(f"Luas Bujur Sangkar bendaSegi4_5 = {bendaSegi4_5.luasBujurSangkar()}")

print(">>> print(f\"Luas Bujur Sangkar bendaSegi4_6 = {bendaSegi4_6.luasBujurSangkar()}\")")
print(f"Luas Bujur Sangkar bendaSegi4_6 = {bendaSegi4_6.luasBujurSangkar()}")

# Display volume of cube
print(">>> print(f\"Volume kubus bendaSegi4_1= {bendaSegi4_1.volumeKubus()}\")")
print(f"Volume kubus bendaSegi4_1= {bendaSegi4_1.volumeKubus()}")

print(">>> print(f\"Volume kubus bendaSegi4_2= {bendaSegi4_2.volumeKubus()}\")")
print(f"Volume kubus bendaSegi4_2= {bendaSegi4_2.volumeKubus()}")

print(">>> print(f\"Volume kubus bendaSegi4_3= {bendaSegi4_3.volumeKubus()}\")")
print(f"Volume kubus bendaSegi4_3= {bendaSegi4_3.volumeKubus()}")

print(">>> print(f\"Volume kubus bendaSegi4_4= {bendaSegi4_4.volumeKubus()}\")")
print(f"Volume kubus bendaSegi4_4= {bendaSegi4_4.volumeKubus()}")

print(">>> print(f\"Volume kubus bendaSegi4_5= {bendaSegi4_5.volumeKubus()}\")")
print(f"Volume kubus bendaSegi4_5= {bendaSegi4_5.volumeKubus()}")

print(">>> print(f\"Volume kubus bendaSegi4_6= {bendaSegi4_6.volumeKubus()}\")")
print(f"Volume kubus bendaSegi4_6= {bendaSegi4_6.volumeKubus()}")

# Display area of persegi panjang
print(">>> print(f\"Luas Persegi Panjang bendaSegi4_1 = {bendaSegi4_1.luasPersegiPanjang()}\")")
print(f"Luas Persegi Panjang bendaSegi4_1 = {bendaSegi4_1.luasPersegiPanjang()}")

print(">>> print(f\"Luas Persegi Panjang bendaSegi4_2 = {bendaSegi4_2.luasPersegiPanjang()}\")")
print(f"Luas Persegi Panjang bendaSegi4_2 = {bendaSegi4_2.luasPersegiPanjang()}")

print(">>> print(f\"Luas Persegi Panjang bendaSegi4_3 = {bendaSegi4_3.luasPersegiPanjang()}\")")
print(f"Luas Persegi Panjang bendaSegi4_3 = {bendaSegi4_3.luasPersegiPanjang()}")

print(">>> print(f\"Luas Persegi Panjang bendaSegi4_4 = {bendaSegi4_4.luasPersegiPanjang()}\")")
print(f"Luas Persegi Panjang bendaSegi4_4 = {bendaSegi4_4.luasPersegiPanjang()}")

print(">>> print(f\"Luas Persegi Panjang bendaSegi4_5 = {bendaSegi4_5.luasPersegiPanjang()}\")")
print(f"Luas Persegi Panjang bendaSegi4_5 = {bendaSegi4_5.luasPersegiPanjang()}")

print(">>> print(f\"Luas Persegi Panjang bendaSegi4_6 = {bendaSegi4_6.luasPersegiPanjang()}\")")
print(f"Luas Persegi Panjang bendaSegi4_6 = {bendaSegi4_6.luasPersegiPanjang()}")

# Display volume of balok
print(">>> print(f\"Volume Balok bendaSegi4_1 = {bendaSegi4_1.volumeBalok()}\")")
print(f"Volume Balok bendaSegi4_1 = {bendaSegi4_1.volumeBalok()}")

print(">>> print(f\"Volume Balok bendaSegi4_2 = {bendaSegi4_2.volumeBalok()}\")")
print(f"Volume Balok bendaSegi4_2 = {bendaSegi4_2.volumeBalok()}")

print(">>> print(f\"Volume Balok bendaSegi4_3 = {bendaSegi4_3.volumeBalok()}\")")
print(f"Volume Balok bendaSegi4_3 = {bendaSegi4_3.volumeBalok()}")

print(">>> print(f\"Volume Balok bendaSegi4_4 = {bendaSegi4_4.volumeBalok()}\")")
print(f"Volume Balok bendaSegi4_4 = {bendaSegi4_4.volumeBalok()}")

print(">>> print(f\"Volume Balok bendaSegi4_5 = {bendaSegi4_5.volumeBalok()}\")")
print(f"Volume Balok bendaSegi4_5 = {bendaSegi4_5.volumeBalok()}")

print(">>> print(f\"Volume Balok bendaSegi4_6 = {bendaSegi4_6.volumeBalok()}\")")
print(f"Volume Balok bendaSegi4_6 = {bendaSegi4_6.volumeBalok()}")