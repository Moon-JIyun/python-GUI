from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly")
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
