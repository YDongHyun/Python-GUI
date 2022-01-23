from tkinter import *

root = Tk()
root.title("GUI")

btn1 = Button(root, text="button 1")
btn1.pack() #창화면에 버튼 추가

btn2 = Button(root,padx=5, pady=10, text="button 2") # 버튼 크기 조정
btn2.pack()

btn3 = Button(root,width=10, height=3, text="button 3") # 버튼 크기 조정
btn3.pack()

btn4 = Button(root,fg="red", bg="yellow", text="button 4") #색 지정
btn4.pack()

photo = PhotoImage(file="C:\\Users\\user\\PycharmProjects\\Python_GUI\\GuIbase\\img.jpg")
btn5 = Button(root,image=photo) # 버튼사진으로
btn5.pack()

def btcmd():
    print("Button Click")

btn6 = Button(root, text="button 6",command=btcmd) # 버튼 커맨드 지정
btn6.pack()

root.mainloop()