# 2차 크롤링 파일 -> 수정본 (간소화)
# 노션에도 있음

import requests
from bs4 import BeautifulSoup
import mysql.connector


def faq(seq,page):
    url = f"https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq={seq}&keyfield=title&listsz=10&cate1={page}&bcd=faq"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    
    
    s = bs.select('tbody td')[3].text
    q = bs.select_one('thead tr').text
    a = bs.select('td.view_contents p')
    num = len(a)
    a_content = ''
    for _ in range(num):
        k = a[_].text
        a_content += k
        
    data_list.append((q, a_content, s))
    print(f"msg_seq {seq} 완료")

num_list = [531, 530, 529, 528, 236, 235, 233, 231, 230, 227, 143, 142, 83, 82, 79, 78]
num_list2 = [120, 119, 118, 117, 116, 115, 114, 113, 112, 109, 108]

connection = mysql.connector.connect(
    host = 'localhost', 
    user = 'ohgiraffers',
    password = 'ohgiraffers',
    database = 'faqdb'
)


cursor = connection.cursor()

data_list = []

for seq in num_list:
    faq(seq,'04')

for seq in num_list2:
    faq(seq,'07')

print(data_list)

for data in data_list:
    sql = "INSERT INTO tbl_faq (faq_title, faq_contents, faq_section) VALUES (%s, %s, %s)"
    print(data)
    cursor.execute(sql,data)

connection.commit()
cursor.close()
connection.close()