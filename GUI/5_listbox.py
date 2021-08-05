from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END,'수박')
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    print(listbox.delete(END))
    #맨 뒤에 항목 삭제

    #갯수 확인
    #print(listbox.size())

    #항목 확인
    #print(listbox.get(0,2))

    #선택된 항목 확인
    #print((listbox.curselection()))


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
