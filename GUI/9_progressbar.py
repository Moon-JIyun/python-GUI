from tkinter import *
import tkinter.ttk as ttk
import  time


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

# progressbar = ttk.Progressbar(root, maximum = 100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum = 100, mode="determinate")
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()
#
# btn = Button(root, text="중단", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar2.update()

btn2 = Button(root, text = "시작", command = btncmd2)
btn2.pack()

root.mainloop()
