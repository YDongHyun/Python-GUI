import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

def info():
    msgbox.showinfo("alim","ok")

def warn():
    msgbox.showwarning("warning","error")

def error():
    msgbox.showerror("error","error")

def okcancel():
    msgbox.askokcancel("yes/no","what")

def retrycancel():
    msgbox.askretrycancel("yes/no", "what")

def yesno():
    msgbox.askyesno("yes/no", "what")

def yesnocancel():
    response=msgbox.askyesnocancel(title=None,message="yes/no/cancel")
    print(response) # true, false, none -> yes->1 , no->0
    if response == 1:
        print("yes")
    elif response == 0:
        print("No")
    else:
        print("cancel")

Button(root, command=info , text="alim").pack()
Button(root, command=warn , text="warning").pack()
Button(root, command=error , text="error").pack()

Button(root, command=okcancel , text="cancel").pack()
Button(root, command=retrycancel , text="cancel").pack()
Button(root, command=yesno , text="yes no").pack()
Button(root, command=yesnocancel , text="yes no cancel").pack()

root.mainloop()