from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

Label(root, text="collect").pack(side="top")

Button(root,text="ok").pack(side="bottom")

frame_burger = Frame(root, relief="solid",bd=1)
frame_burger.pack(side="left", fill="both",expand=True)

Button(frame_burger, text="hamburger").pack()
Button(frame_burger, text="hamburger2").pack()
Button(frame_burger, text="hamburger3").pack()

frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink, text="cola").pack()
Button(frame_drink, text="sidarr").pack()

root.mainloop()
