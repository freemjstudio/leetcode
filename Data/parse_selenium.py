import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 크롬 드라이버 객체 생성
driver = webdriver.Chrome()

# 페이지 열기
url = "https://www.shinhan.com/hpe/index.jsp#050101010000"
driver.get(url)

##click to 대출
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/ul/li[3]/a').click()

q_list=[]

##click to 질문
for Z in range(2):
    for k in range(10):
        # page = driver.find_element(By.XPATH, number[k])
        # page.send_keys(Keys.ENTER)
        time.sleep(3)
        for i in range(1,11):
            print(i)
            q_path=f'/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/table/tbody/tr[{i}]/td[2]'
            driver.find_element(By.XPATH, q_path).click()
            time.sleep(3)
            ##get text
            dt_elements = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/dl/dt")
            dd_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/dl/dd")
            dt_list = []
            dd_list = []
            time.sleep(2)
            for i in range(len(dt_elements)):
                dt = dt_elements[i].text.replace("\n"," ").strip()
                dd = dd_elements[i].text.replace("\n"," ").strip()
                dt_list.append(dt)
                dd_list.append(dd)
                dict_elements={'Instruction':dt_list[0].replace("\n"," "),'Context':'','Response':dd_list[0].replace("\n"," "),'Category':'open_qa'}
            q_list.append(dict_elements)
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/a').click()
            time.sleep(5)
#다음페이지
    pagedown = driver.find_element(By.XPATH, f'//*[@id="page_last_{i}"]')
    pagedown.send_keys(Keys.ENTER)
    time.sleep(1)
