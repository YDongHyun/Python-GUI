from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기
#root.geometry("640x480+300+100") 가로 * 세로크기 and x좌표 +y좌표

root.resizable(True, False) #x, y 값 변경 불가 (창크기 고정)

root.mainloop()


