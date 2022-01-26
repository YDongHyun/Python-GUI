from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

# 라디오 버튼은 여러개 중 택 1
Label(root,text="select").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root,text="hamburger",value=1,variable=burger_var)
btn_burger1.select() # 기본 선택
btn_burger2 = Radiobutton(root,text="cheese hamburger",value=2,variable=burger_var)
btn_burger3 = Radiobutton(root,text="chicken hamburger",value=3,variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root,text="cola",value="cola",variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root,text="sidar",value="sidar",variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()
