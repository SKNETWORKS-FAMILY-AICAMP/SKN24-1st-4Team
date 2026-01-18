## 1차 크롤링


import requests
from bs4 import BeautifulSoup


#url 리스트
# 1) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=275&keyfield=title&listsz=10&cate1=07&bcd=faq
# 2) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=120&keyfield=title&listsz=10&cate1=07&bcd=faq
# 3) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=119&keyfield=title&listsz=10&cate1=07&bcd=faq
# 4) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=118&keyfield=title&listsz=10&cate1=07&bcd=faq
# 5) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=117&keyfield=title&listsz=10&cate1=07&bcd=faq
# 6) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=116&keyfield=title&listsz=10&cate1=07&bcd=faq
# 7) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=115&keyfield=title&listsz=10&cate1=07&bcd=faq
# 8) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=114&keyfield=title&listsz=10&cate1=07&bcd=faq
# 9) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=113&keyfield=title&listsz=10&cate1=07&bcd=faq
#10) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=112&keyfield=title&listsz=10&cate1=07&bcd=faq
# 11) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=109&keyfield=title&listsz=10&cate1=07&bcd=faq&pgno=2
# 12) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=108&keyfield=title&listsz=10&cate1=07&bcd=faq&pgno=2
# 13) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=531&keyfield=title&listsz=10&cate1=04&bcd=faq
# 14) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=530&keyfield=title&listsz=10&cate1=04&bcd=faq
# 15) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=529&keyfield=title&listsz=10&cate1=04&bcd=faq
# 16) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=528&keyfield=title&listsz=10&cate1=04&bcd=faq
# 17) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=236&keyfield=title&listsz=10&cate1=04&bcd=faq
# 18) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=235&keyfield=title&listsz=10&cate1=04&bcd=faq
# 19) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=233&keyfield=title&listsz=10&cate1=04&bcd=faq
# 20) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=231&keyfield=title&listsz=10&cate1=04&bcd=faq
# 21) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=230&keyfield=title&listsz=10&cate1=04&bcd=faq
# 22) https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=227&keyfield=title&listsz=10&cate1=04&bcd=faq

#=========================

# 혼잡 키워드
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=275&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

print('1번')
#<질문 제목>=faq title
q=bs.select_one('thead th')
print(q.text)

#<질문 답변>=faq contents
a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4)')
if a:
    contents =a.select('p')
    #contents -> 변수로 만듦
    # #p=tag
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
#'a', 'a_contets'는 변수명
#strip는 공백 제거 도우미
#for  in: -> 예약어 -> 반복 시작
#append -> 추가
#\n:줄바꿀 수 있음 -> 줄바꿈 1번 가능
#\n\n:줄바꿈 2번 가능 (\n 늘어날수록 그만큼 줄바꿈 많이 가능)
print(a)
#.붙이면 class 됨!!

#<질문 구분>=faq section
b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

# memo
# <b(변수명=질문구분)을 왜 이렇게 했는지>
# 1) b=[질문 구분]->[혼잡통행료]를 프린트하려는데 계속 상위인 [교통부대시설처]가 프린트되서 
# 2) Devetools에서 selector버전으로 카피함
# 3) 이렇게 하니까 잘됐어요!

#<a(변수명=faq_contents))를 왜 이렇게 했는지>
# 1) 'tbody p'로 출력하면 한 단락 내용만 나옴
# 2) 그래서 유일하게 이해한 'if ~ in :' 코드 이용했습니다!!!
# 3) 그랬더니 모든 단락 프린트가 됐어요!


#==============

print('2번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=120&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('3번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=119&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('4번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=118&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('5번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=117&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)


#==============

print('6번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=116&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('7번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=115&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('8번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=114&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('9번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=113&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('10번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=112&keyfield=title&listsz=10&cate1=07&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('11번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=109&keyfield=title&listsz=10&cate1=07&bcd=faq&pgno=2"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============

print('12번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=108&keyfield=title&listsz=10&cate1=07&bcd=faq&pgno=2"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)


#==============
#교통 키워드
print('13번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=531&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('14번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=530&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('15번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=529&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('16번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=528&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('17번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=236&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('18번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=235&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('19번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=233&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('20번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=233&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('21번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=230&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)

#==============
#교통 키워드
print('22번')
url = "https://www.sisul.or.kr/open_content/traffic/bbs/bbsMsgDetail.do?msg_seq=227&keyfield=title&listsz=10&cate1=04&bcd=faq"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

q=bs.select_one('thead th')
print(q.text)

a=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(4) > td')
if a:
    contents =a.select('p')
    a_list=[]
    for a in contents:
        if not a.find('img'):
            text=a.get_text(strip=True)
            text=text.replace("-","")
            if text:
                a_list.append(text)
    a='\n\n'.join(a_list)
else:
    a='X'
print(a)

b=bs.select_one('#detail_con > div > table > tbody > tr:nth-child(3) > td:nth-child(2)')
print(b.text)
