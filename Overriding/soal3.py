'''
This code was created by Robanu Dakhayin
'''

class BendaBulat :

    def __init__(self, radius, warna) -> None:
        self.__radius = radius
        self.__warna = warna

    def getRadius(self) : return self.__radius

    def getWarna(self) : return self.__warna

    def display(self) :
        print(f"Warna = {self.getWarna()}")
        print(f"Radius = {self.getRadius()}")

class Tabung(BendaBulat) :

    def __init__(self, radius, warna, tinggi) -> None:
        super().__init__(radius, warna)
        self.__tinggi = tinggi

    def getTinggi(self) : return self.__tinggi

    def display(self):
        super().display()
        print(f"Tinggi = {self.getTinggi()}")
    
    def luasPermukaanTabung(self) :
        return 3.14 * self.getRadius() * (self.getTinggi() + (2 * self.getRadius()))
    

# Main class
# Create object
tb1 = Tabung(radius= 10, warna= "red", tinggi= 15)
bb1 = BendaBulat(radius= 10, warna= "blue")
tb2 = Tabung(radius= 20, warna= "purple", tinggi= 15)

# Call method display and luasPermukaanTabung
print("====Object tb1====")
tb1.display()
print(f'Luas permukaan = {tb1.luasPermukaanTabung()}')

print("\n====Object bb1====")
bb1.display()

print("\n====Object tb2====")
tb2.display()
print(f'Luas permukaan = {tb2.luasPermukaanTabung()}')