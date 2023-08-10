from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd


chromedriver_autoinstaller.install()
drive = webdriver.Chrome()

id_url_list = []

#여기에 원하는 키워드 입력하세요
keyword = '키워드 입력'
repeatPages = 5

for i in range(0, repeatPages):
    # 페이지 이동
    web_url = f"https://section.blog.naver.com/Search/Post.naver?pageNo={i}&rangeType=ALL&orderBy=sim&keyword={keyword}"
    drive.get(web_url)

    id_url = drive.find_elements_by_class_name('author')

    for i in id_url:
        id_url_list.append(i.get_attribute('href'))
        drive.implicitly_wait(10)
    # time.sleep(1)
    drive.implicitly_wait(10)

id_list = []
for i in id_url_list:
    result = i.split('/')
    id_list.append(result[3])

# # 중복된 아이디 제거
set_list = set(id_list)
# # set형식을 list로 변환
final_id_list = list(set_list)
data = pd.DataFrame(final_id_list)
# mode = a 를 추가해 기존에 있던 csv를 append, 즉 overwrite형식으로 변경
data.to_csv('naver_blogId_키워드.csv', mode='a', header=False, index=False)

drive.quit()


