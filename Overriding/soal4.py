'''
This code was created by Robanu Dakhayin
'''

class BendaPersegi :

    def __init__(self, panjang, lebar, warna= None) -> None:
        self.__warna = "Blue" if(warna == None) else warna
        self.__panjang = panjang
        self.__lebar = lebar

    def getPanjang(self) : return self.__panjang

    def getLebar(self) : return self.__lebar

    def getWarna(self) : return self.__warna

    def display(self) :
        print(f'Panjang = {self.getPanjang()}')
        print(f'Lebar = {self.getLebar()}')
        print(f'Warna = {self.getWarna()}')

class Balok(BendaPersegi) :

    def __init__(self, panjang, lebar, tinggi, warna=None) -> None:
        super().__init__(panjang, lebar, warna)
        self.__tinggi = tinggi

    def getTinggi(self) : return self.__tinggi

    def display(self):
        super().display()
        print(f'Tinggi = {self.getTinggi()}')

    def volume(self) :
        return super().getPanjang() * super().getLebar() * self.getTinggi()


# Main Class
# Create object
bb1 = Balok(panjang= 10, lebar= 5, tinggi= 8)
bp1 = BendaPersegi(panjang= 10, lebar= 10)
bb2 = Balok(panjang= 20, lebar= 15, tinggi= 12, warna= "Red")
bp2 = BendaPersegi(panjang= 6, lebar= 6, warna= "Purple")

# Call method
print("====Object bb1====")
bb1.display()
print(f'Volume = {bb1.volume()}')

print("\n====Object bp1====")
bp1.display()

print("\n====Objext bb2====")
bb2.display()
print(f'Volume = {bb2.volume()}')

print("\n====Object bp2====")
bp2.display()