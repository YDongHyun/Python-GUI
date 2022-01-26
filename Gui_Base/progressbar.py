import time
import tkinter.ttk as ttk #progressbar
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기
#
# progressbar = ttk.Progressbar(root, maximum= 100, mode = "indeterminate") #mode값. 언제끝날지 모를 때
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()
#
# progressbar2 = ttk.Progressbar(root, maximum= 100, mode = "determinate") #차는 모습
# progressbar2.start(10) #10ms 마다 움직임
# progressbar2.pack()
#
# def btncmd():
#     progressbar.stop() # 작동중지;
#
# btn = Button(root,text="stop",command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100 , length=150, variable=p_var2)
progressbar3.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) # 대기

        p_var2.set(i) # progressbar 값 설정
        progressbar3.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root,text="start",command=btncmd2)
btn.pack()

root.mainloop()