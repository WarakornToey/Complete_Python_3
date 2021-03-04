from tkinter import * 

def leftClickButton(event): #event เหตุการณ์ในการกดของ User 
    print("Left Click !!")

def doubleClickButton(event):
    print("Double Click !!")

main = Tk()
button = Button(main,text="My Button !!")
button.pack()
button.bind('<Button-1>',leftClickButton) #'<Button-1>' ปุ่มซ้ายสุดของ Mouse , <Button-2> ปุ่มตรงกลาง , <Button-3> ปุ่มคลิกขวา
button.bind('<Double-1>',doubleClickButton)
main.mainloop()