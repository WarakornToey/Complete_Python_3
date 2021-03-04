class Vehicle: # Class หลัก
     licenseCode = ""
     serialCode = ""
     face_ID = ""
     def turnOnAir(self):
        print("Turn On Air")

class Car(Vehicle): # class สืบทอด
    def turnOnAir(self):  # ทำ Overriding แม้ Function จะประกาศเหมือนกัน
        print("Hello Car Test Overriding")
    
class Pickup(Vehicle): # class สืบทอด
    def turnOnAir(self):
        print("Hello Pickup Test Overriding")

class Van(Vehicle): # class สืบทอด
    def turnOnAir(self):
        print("Hello Van Test Overriding")

class Estatecar(Vehicle): # class สืบทอด
    def turnOnAir(self):
        print("Hello Estatecar Test Overriding")

Car1 = Car()
Car1.turnOnAir()  # ผลลัพธ์การทำ Overiding

Pickup2 = Pickup()
Pickup2.turnOnAir()

Van1 = Van()
Van1.turnOnAir()

Estatecar1 = Estatecar()
Estatecar1.turnOnAir()