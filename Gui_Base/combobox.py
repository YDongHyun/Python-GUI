import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

values=[str(i) + "일" for i in range(1,32)] # 1~31의 숫자를 받음
combobox = ttk.Combobox(root,height=5 , values=values)
combobox.pack()
combobox.set("day") #최초 목록 제목 설정

ro_combobox = ttk.Combobox(root,height=5 , values=values, state = "readonly") # 읽기전용
ro_combobox.current(0) #번째를 제목 설정
ro_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택값 표시

btn = Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()