from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

chkvar=IntVar() #chkvar에 int형으로 값을 저장
chkbox=Checkbutton(root,text="오늘 안보기",variable=chkvar)
chkbox.select() #자동 선택 처리 / deselect
chkbox.pack()

chkvar2=IntVar() #chkvar에 int형으로 값을 저장
chkbox2=Checkbutton(root,text="일주일 안보기",variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 = 체크 해제 / 1 = 체크
    print(chkvar2.get())

btn = Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()