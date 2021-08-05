from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.filedialog as fileDialgo
import os

root = Tk()
root.title("제목없음 - MacOS 메모장")

root.geometry("640x480") # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

def openfile():
    filename = fileDialgo.askopenfilename(initialdir="/", title="Select file",
                                            filetypes=(("txt files", "*.txt"),
                                                       ("all files", "*.*")))

    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())


def savefile():
    filename = fileDialgo.asksaveasfilename(initialdir="/", title="*.txt",
                                            filetypes=(("txt files", "*.txt"),
                                                       ("all files", "*.*")))

    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)

#File Menu
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "열기", command = openfile)
menu_file.add_command(label = "저장", command = savefile)
menu_file.add_separator()
menu_file.add_command(label = "끝내기", command = root.quit)
menu.add_cascade(label = "파일", menu = menu_file)

#스크롤바 추가
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "both")

#txt 창 추가
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(fill ="both", expand = True)

scrollbar.config(command = txt.yview)


root.config(menu = menu)
root.mainloop()
