from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

Label(root, text="메뉴를 선택해주세요").pack(side="top")



frame_burger = LabelFrame(root, relief = "solid", bd=1)
frame_burger.pack(side ="left", fill="both",expand = True)


Button(frame_burger, text = "불고기버거").pack()
Button(frame_burger, text = "치즈버거").pack()
Button(frame_burger, text = "치킨버거").pack()

frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side ="right", fill="both",expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()
