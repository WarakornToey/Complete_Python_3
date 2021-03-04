class Animal():
    def eat(self):
        print("Eating Eating !!")

class Cat (Animal):
    __name = "" #__name การตั้งค่าตัวเเปรไม่ให้เรียกใช้งานจากข้างนอก
    def setName(self,text): #Getter ฟังก์ชันที่จะดึงออกมาตรง ๆ 
        self.name = text    #Setter ฟังก์ชันในการกำหนดค่า
        print("Setting New Cat Name = ",self.name)
    def eat(self):
        print("Meoww !!",self.name)

cat1 = Cat()
cat1.setName("Fuu")
#print(cat1.__name)  #เวลาเรียกใช้งานต้องเรียกใช้งานผ่านฟังก์ชันนั้น ๆ 
cat1.eat()
