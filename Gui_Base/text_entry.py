from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

txt = Text(root, width=30, height =5) #txt 입력 창
txt.pack()

txt.insert(END,"글자를 입력") #hint txt

e=Entry(root,width=30) #엔트리 생성 / 엔터 x 한줄만 입력 가능
e.pack()
e.insert(0,"한줄만 입력")  #hint txt

def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) #1= 첫번째 라인 0= 0번째 column
    print(e.get())\

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()
