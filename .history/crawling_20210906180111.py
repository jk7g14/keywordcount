from requests_html import HTML, HTMLSession
from time import sleep
import csv
import datetime


file = open(f'data-{datetime.datetime.now()}', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["name", "date", "content"])


session = HTMLSession()
url = 'https://www.ybtour.co.kr/promotion/incRepList.yb'
data = {'bnrMstNo': 20000016490, 'pageNo': 1}

while(True):
    r = session.post(url, data=data)
    items = r.html.find('.box_prom_temp .desc_cmt')
    if len(items) == 0:
        break
    for item in items:
        name = item.find('.list_user .name', first=True).text
        date = item.find('.list_user .date', first=True).text
        content = item.find('.txt_desc', first=True).text
        writer.writerow([name, date, content])
        print(f'작성자: {name}, 작성일: {date} \n')
        print(f'---------------------------------- \n')
        print(f'내용: {content}')
        print('------------------------------------------------------')
    data['pageNo'] += 1
    print(f'{data["pageNo"]}페이지 진행중')
    sleep(1)

file.close()
print('---------------------------완료')
print('---------------------------완료')
print('---------------------------완료')
print('---------------------------완료')
