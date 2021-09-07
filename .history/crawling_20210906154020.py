from requests_html import HTML, HTMLSession
from time import sleep

session = HTMLSession()
r = session.get(
    'https://www.ybtour.co.kr/promotion/eventDetail.yb?mstNo=20000016490&pageNo=1')
