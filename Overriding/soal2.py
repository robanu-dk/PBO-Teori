'''
This code was created by Robanu Dakhayin
'''

class Vehicle :

    def start(self) -> None:
        print("Vehicle start code")

    def stop(self) -> None:
        print("Vehicle stop code\n")

class Car(Vehicle) :

    def __init__(self) -> None :
        self.__nbOfSeats = 0

    def setNbOfSeats(self, nbOfSeats) -> None :
        self.__nbOfSeats = nbOfSeats

    def start(self) -> None:
        print("Car Start Code")

    def getNbOfSeats(self) -> int :
        return self.__nbOfSeats


# Main class

# Create object
car1 = Car()
vehiclel1 = Vehicle()
car2 = Car()

print("====Object car1====")
car1.start()
car1.setNbOfSeats(nbOfSeats=6)
print(f'nbOfSeats = {car1.getNbOfSeats()}')
car1.stop()

print("====Object vehicle====")
vehiclel1.start()
vehiclel1.stop()

print("====Object car2====")
car2.start()
car2.setNbOfSeats(nbOfSeats=8)
print(f'nbOfSeats = {car2.getNbOfSeats()}')
car2.stop()