from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
# 네이버 아이디 복붙용
import pyperclip
import clipboard
# 서이웃 그룹 생성용
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from collections import defaultdict
import json


# 크롤링 옵션 생성
options = webdriver.ChromeOptions()
# 백그라운드 실행 옵션 추가
options.add_argument("headless")
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

chromedriver_autoinstaller.install()
drive = webdriver.Chrome()



# 서이추 시작
# 해당 웹사이트를 가서 네이버 로그인
url = 'https://nid.naver.com/nidlogin.login'
# 접속
drive.get(url)

drive.implicitly_wait(10)            

# 페이지가 로딩될 때까지 잠시 대기
time.sleep(5)

#본인의 아이디와 비밀번호를 입력
uid = "id"
upw = "pw"

#아이디 입력

#clipboard.copy(uid)
pyperclip.copy(uid)
drive.find_element_by_id("id").send_keys(Keys.COMMAND , 'V')
time.sleep(1)
#비번 입력
#clipboard.copy(upw)
pyperclip.copy(upw)
drive.find_element_by_id("pw").send_keys(Keys.COMMAND , 'V')
time.sleep(1)

# 작업 10초
drive.implicitly_wait(10)

# # classes > 복수값
# # id &&  >고유값
drive.implicitly_wait(5)
drive.find_element_by_css_selector('#log\.login').click()

drive.implicitly_wait(20)

df = pd.read_csv('naver_blogId_키워드.csv', header=None)[0]

msg = '''서로이웃추가 메시지 작성란'''

for id in df:
    try:
        print(id)
        blog_url = 'https://m.blog.naver.com/BuddyAddForm.naver?blogId='+ id # +'&returnUrl=https%253A%252F%252Fm.blog.naver.com%252Fhiksoo'
        drive.get(blog_url)

        # 서이추 기능이 disable일 시 다음 id로 넘김
        exceptional_text = drive.find_elements_by_class_name('dsc')[0].text
        conditions = [drive.find_element_by_id('bothBuddyRadio').is_enabled(),
                       "제한된" not in exceptional_text,
                       "진행중" not in exceptional_text,
                       '하루에' not in exceptional_text]
        # 오류
        
        # True
        if False not in conditions:
            # 서이추 버튼 클릭
            # implicitly_wait을 통한 작업 소요시간 고려
            drive.find_element_by_id('bothBuddyRadio').click()
            drive.implicitly_wait(5)

            # 미리 입력된 기본값을 지운다.
            drive.find_element_by_tag_name('textarea').clear()
            drive.find_element_by_tag_name('textarea').send_keys(msg)
            drive.implicitly_wait(5)        

            # 확인 버튼 누르기
            drive.find_element_by_class_name('btn_ok').click()
            drive.implicitly_wait(5)      

        
        time.sleep(0.5)
    except Exception as e:
        print('error?', e)
        pass



