from requests_html import HTML, HTMLSession
from time import sleep

session = HTMLSession()
url = 'https://www.ybtour.co.kr/promotion/incRepList.yb'
data = {'bnrMstNo': 20000016490, 'pageNo': 1}

r = session.post(url, data=data)
items = r.html.find('.box_prom_temp .desc_cmt')
for item in items:
    name = item.find('.list_user .name', first=True).text
    date = item.find('.list_user .date', first=True).text
    content = item.find('.txt_desc', first=True).text
    print(f'작성자: {name}, 작성일: {date}, 내용: {content}')
    print('------------------------------------------------------')
