from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") #가로 * 세로크기

def create_new_file():
    print("newfile")

menu=Menu(root)


# file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open file.")
menu_file.add_separator()
menu_file.add_command(label="Save all", state="disable") # 비활성화
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File",menu=menu_file)

#edit 메뉴
menu.add_cascade(label="Edit")

#language 메뉴 추가 (라디오 버튼처럼 사용 가능)
menu_lang=Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Language",menu=menu_lang)

#view 메뉴 (체크버튼)
menu_view=Menu(menu, tearoff=0)
menu_view.add_radiobutton(label="Show minimap")
menu.add_cascade(label="view",menu=menu_view)

root.config(menu=menu)
root.mainloop()