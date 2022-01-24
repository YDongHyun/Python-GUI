from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

listbox=Listbox(root,selectmode="extended",height=0) #리스트 생성 selectmode -> single도 있음 / height는 한번에 보이는 목록 수
listbox.insert(0,"apple")
listbox.insert(1,"banana")
listbox.insert(2,"melon")
listbox.insert(END,"graph")
listbox.insert(END,"kiwi")
listbox.pack()

def btncmd():
    listbox.delete(END) #맨뒤에 리스트 삭제

    print(listbox.size()) #항목 개수

    print(listbox.get(0,2)) # 1~3항목 출력

    print(listbox.curselection()) #선택된 항목 확인 (위치로 반환)

btn = Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()
