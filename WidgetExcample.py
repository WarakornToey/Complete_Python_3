from tkinter import *

def sayHello():
    print("Hello Toey")

MainWindow = Tk() #สร้าง Tkinter คือตัวหลักในการจัดการ GUI
button = Button(MainWindow,text="Click Me1",command = sayHello()).grid(row=0,column=1) #Widget ต้องสร้างหลังจาก MainWindow ,text Attribute ,command กำหนดฟังก์ชันการทำงาน
button2 = Button(MainWindow,text="Click Me2",command = sayHello()).grid(row=1,column=1) #.grid(row=...)การจัดการ Layout Button
button3 = Button(MainWindow,text="Click Me3",command = sayHello()).grid(row=0,column=2)
MainWindow.mainloop()