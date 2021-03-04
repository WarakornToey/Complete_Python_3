from tkinter import * 
main = Tk()

text1 = Label(main,text="Hello Toey",width=20,fg="red",bg="blue",font=("Helveteca",76),anchor=CENTER).grid(row=0,column=1)
main.mainloop()
 
# กำหนดขนาด font=("Helveteca"),76) , anchor=W ตัวอักกษรชิดซ้าย , anchor=E ชิดขวา , anchor=CENTER กึ่งกลาง
