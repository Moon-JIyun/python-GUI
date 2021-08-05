from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warning():
    msgbox.showwarning("해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("결제 오류")

def okcancel():
    msgbox.askokcancel("확인/ 취소","해당 좌석은 유아동반석 입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycance("확인/ 취소","일시적 오류입니다. 재시도 하시겠습니까?")
    if response == 1:
        print("예")
    elif response==0:
        print("취소")

def yesno():
    msgbox.askyesno("예/아니오", "해당 좌석은 역방향입니다., 예매하시겠습까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다." "\n 저장 후 종료하시겠습니까?")
    print("응답:", response)
    if response == 1:
        print("예")
    elif response==0:
        print("아니오")
    else:
        print("취소")


Button(root, command=info, text="예약").pack()
Button(root, command=warning, text="매진").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()





root.mainloop()
