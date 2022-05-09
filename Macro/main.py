import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
import macro
import os

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(BASE_DIR + '/macro.ui')[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    stop_signal = pyqtSignal()

    id = ""
    pw = ""
    url = ""
    menuid = ""
    keyword = ""
    comment = ""

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pw_lineEdit.setEchoMode(QLineEdit.Password)

        self.idCheckBtn.clicked.connect(self.idCheck)
        self.pwCheckBtn.clicked.connect(self.pwCheck)
        self.urlCheckBtn.clicked.connect(self.urlCheck)
        self.menuLinkCheckBtn.clicked.connect(self.menuIdCheck)
        self.keywordCheckBtn.clicked.connect(self.keywordCheck)
        self.commentCheckBtn.clicked.connect(self.commentCheck)
        self.runBtn.clicked.connect(self.run)
        self.stopBtn.clicked.connect(self.stop_thread)



    def idCheck(self):
        self.id = self.id_lineEdit.text()
        print("id:", self.id)

    def pwCheck(self):
        self.pw = self.pw_lineEdit.text()
        print("pw:", self.pw)

    def urlCheck(self):
        self.url = self.urlLineEdit.text()
        print("url:", self.url)

    def menuIdCheck(self):
        self.menuid = self.menuLink.text()
        print("menuid:", self.menuid)

    def keywordCheck(self):
        self.keyword = self.keywordLineEdit.text()
        print("keyword:", self.keyword)

    def commentCheck(self):
        self.comment = self.commentLineEdit.text()
        print("comment:", self.comment)

    def run(self):
        # Thread
        if self.id != "" and self.pw != "" and self.url != "" and self.menuid != "" and self.keyword != "" and self.comment != "":
            self.thread = QThread()
            self.worker = macro.Worker(self)
            # self.worker.moveToThread(self.thread)
            #
            # self.thread.started.connect(self.worker.runMacro)
            # self.worker.finished.connect(self.thread.quit)
            # self.worker.finished.connect(self.worker.deleteLater)
            # self.thread.finished.connect(self.thread.deleteLater)

            self.worker.start()

        else:
            QMessageBox.question(self, "Message", "빈 값이 있습니다.", QMessageBox.Close, QMessageBox.NoButton)



    def stop_thread(self):
        self.stop_signal.emit()
        self.worker.stop()



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()