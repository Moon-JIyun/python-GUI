from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)


txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width = 30)  # 한줄로 입력 받을 때, Entry 사
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 행, 0: 0번째 열 위치
    print(e.get())

    #내용삭제
    txt.delete("1.0", END)
    e.delete(0,END)


btn = Button(root, text="click", command = btncmd)
btn.pack()

root.mainloop()
