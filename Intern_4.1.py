import requests
from bs4 import BeautifulSoup

URL = 'https://theinternship.io/'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
fromhtml = soup.find_all('div',class_='column is-one-third-desktop is-half-tablet')
data = []
for i in fromhtml :
    data.append({'img':i.img['src'],'lentext':len(i.text)})

def lentext(data):
    return data.get('lentext')
data.sort(key=lentext)

for d in data :
    print(d['img'])
    ######### บางรูปไม่ได้อยู่ใน company/ ???????  #########
    # print('company/'+d['img'].replace('company/',''))
    # URL ของ รูป