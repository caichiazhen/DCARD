from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

#設定webdriver及網址
path = r"C:\Users\CCZ\Desktop\chromedriver.exe"
driver = webdriver.Chrome(path)
url = 'https://www.dcard.tw/f'
driver.get(url)

#在搜尋的輸入框內輸入文字
inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('軟體工程師')

#點擊「搜尋按鈕」
driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)#休息兩秒鐘才能回傳搜尋結果

#擷取網站內容，並解析成html結構樹
html = driver.page_source
soup = bs(html, 'html.parser')

#獲得文章看板、作者、時間
meta_datas = []
for x in soup.find_all('span', {'class':'sc-6oxm01-2 hiTIMq'}):
    meta_datas.append(x.text.strip())
print(meta_datas)

#從meta_datas裡面跳出「看板」
forums = []
author = []
times = []
for i in range(len(meta_datas)):
    if i % 3 == 0:
        forums.append(meta_datas[i])
    if i % 3 == 1:
        author.append(meta_datas[i])
    if i % 3 == 2:
        times.append(meta_datas[i])



#獲得文章標題
titles = []
for x in soup.find_all('h2',{'class' : 'sc-1v1d5rx-3 eihOFJ'}):
    titles.append(x.text)
print(titles)

#獲得文章連結
hrefs = []
for x in soup.find_all('a', {'class': 'sc-1v1d5rx-4 gCVegi'}):
    hrefs.append(x['href'])

#從相對連結及url組成絕對連結
links = []
for href in hrefs:
    links.append(urljoin(url, href))
print(links)

#印出「看板、標題、連結」
for i in range(len(forums)):
    print(forums[i], titles[i], links[i])