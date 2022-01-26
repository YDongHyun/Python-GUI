from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

# btn1= Button(root,text='button1')
# btn2= Button(root,text='button2')
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

btn_f16=Button(root,text="F16",padx=10, pady=10) #상하 좌우 크기 변경
btn_f17=Button(root,text="F17")
btn_f18=Button(root,text="F18")
btn_f19=Button(root,text="F19")

btn_f16.grid(row=0, column=0,sticky=N+E+W+S,padx=4, pady=3) # sticky 지정한 방향으로 버튼을 늘림, padx,y는 여백
btn_f17.grid(row=0, column=1,sticky=N+E+W+S)
btn_f18.grid(row=0, column=2,sticky=N+E+W+S)
btn_f19.grid(row=0, column=3,sticky=N+E+W+S)

#clear 줄
btn_clear = Button(root,text="clear",width=5, height=2)
btn_equal = Button(root,text="=")
btn_div = Button(root,text="/")
btn_mul = Button(root,text="*")

btn_clear.grid(row=1,column=0,sticky=N+E+W+S)
btn_equal.grid(row=1,column=1,sticky=N+E+W+S)
btn_div.grid(row=1,column=2,sticky=N+E+W+S)
btn_mul.grid(row=1,column=3,sticky=N+E+W+S)

btn_enter=Button(root,text="enter")
btn_enter.grid(row=4,column=3, rowspan=2,sticky=N+E+W+S) #세로로 합침 가로는 columnspan

root.mainloop()