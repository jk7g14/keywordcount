from requests_html import HTML, HTMLSession
from time import sleep

session = HTMLSession()
url = 'https://www.ybtour.co.kr/promotion/incRepList.yb'
data = {'bnrMstNo': 20000016490, 'pageNo': 1}

r = session.post(url, data=data)
items = r.html.find('.box_prom_temp .desc_cmt')
print(items)
