from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)  # 스크롤바 추가
scrollbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended",height=10,yscrollcommand = scrollbar.set)


for i in range(1,32):
    listbox.insert(END, str(i)+"일")
listbox.pack()

scrollbar.config(command=listbox.yview)

root.mainloop()