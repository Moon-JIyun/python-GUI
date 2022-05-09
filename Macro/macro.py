from urllib.request import urlopen  # 주소를 열기 위해 사용
from urllib.parse import quote_plus # 문자를 url에 알맞은 형태로 치환하기 위해 사용
from bs4 import BeautifulSoup
from selenium import webdriver
import sys, os, time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Worker(QThread):
    finished = pyqtSignal()
    status = pyqtSignal(bool)


    def __init__(self, parent):
        QThread.__init__(self, parent=parent)
        self.continue_run = True
        self.parent = parent

    def date_parser(self, date):
        s = str(date)
        s = s.lstrip('<td class="td_date">')
        date = s.rstrip('.</td>')
        # if len(s) >= 10:
        #     date_format = '%Y.%m.%d'
        # else:
        #     date_format = '%H:%M'
        # date =  datetime.strptime(s, date_format)
        return date

    def run(self):

        id = self.parent.id
        pw = self.parent.pw
        url = self.parent.url
        menuid = self.parent.menuid
        keyword = self.parent.keyword
        comment = self.parent.comment

        # if getattr(sys, 'frozen', False):
        #     chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver")
        #     driver = webdriver.Chrome(chromedriver_path)
        # else:
        driver = webdriver.Chrome(r'/Users/jiyunmoon/Desktop/programming/Macro/chromedriver')
        # r'/Users/jiyunmoon/Desktop/programming/Macro/chromedriver'

        # 네이버에 먼저 로그인하기
        driver.get('https://naver.com')
        driver.find_element_by_xpath('//*[@id="account"]/a').click()
        driver.execute_script("document.getElementsByName('id')[0].value = \'" + id + "\'")
        time.sleep(1)
        driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
        time.sleep(1)
        # 매크로 탐지를 회피하기 위한 자바스크립트 사용
        driver.find_element_by_xpath('//*[@id="log.login"]').click()

        # 원하는 카페 접속
        driver.get('https://cafe.naver.com/'+url)
        driver.find_element_by_xpath('//*[@id="menuLink'+menuid+'"]').click()
        time.sleep(1)

        # 공지 찾기
        driver.switch_to.frame('cafe_main') # 프레임을 게시판 프레임으로 변경

        keyword = keyword
        comment = comment

        notice = "gnr.notice"
        # article = "gnr.article"

        block1 = '//*[@id="upperArticleList"]/table/tbody/tr['
        block2 = ']/td[1]/div[2]/div/a[1]'


        count = 1
        while self.continue_run:
            pageString = driver.page_source
            bsObj = BeautifulSoup(pageString, 'html.parser')
            title = bsObj.find_all(class_="article")
            date = bsObj.find_all(class_="td_date")
            time.sleep(0.05)
            #페이지가 새로고침될 때 마다 페이지 정보를 받아와 title에 저장
            for i in title:
                if i.get('onclick') == None:
                    break
                if notice in i['onclick']:
                    print(i.getText().strip())
                    day = self.date_parser(date[count-1])
                    print("Day::", day)
                    if (keyword in i.getText().strip()) and len(day) < 10:
                        print("COUNT::", count)
                        xpath = block1 + str(count) + block2
                        driver.find_element_by_xpath(xpath).click()
                        time.sleep(0.5)

                        # 댓글창 클릭 ( 100개 넘어간 뒤 개선 필요 )

                        driver.find_element_by_xpath(
                            '//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div[2]/div[1]/textarea').send_keys(comment)
                        driver.find_element_by_xpath(
                            '//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/a').click()
                        self.continue_run = False
                        self.finished.emit()
                        break
                        # 조건에 맞는 게시물을 찾으면 접속하고 success를 false로 변경
                    count += 1
                else:
                    break
            count = 1
            if self.continue_run:
                driver.switch_to.parent_frame()
                driver.find_element_by_xpath('//*[@id="menuLink'+menuid+'"]').click()
                driver.switch_to.frame('cafe_main')
                time.sleep(0.05)
                # 찾지 못했을 경우 새로고침 대신 다시 게시판에 들어오는 과정을 거침
            self.finished.emit()


    def stop(self):
        self.continue_run = False






