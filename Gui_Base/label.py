from tkinter import *

root = Tk()
root.title("GUI")

label1 = Label(root, text="hello") #창화면에 글 출력
label1.pack()

photo = PhotoImage(file="C:\\Users\\user\\PycharmProjects\\Python_GUI\\Gui_Base\\img.jpg")

label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="see you") #글 바뀜
    label2.config(image=photo) #사진 변경

btn= Button(root, text="click",command=change)
btn.pack()

root.mainloop()
