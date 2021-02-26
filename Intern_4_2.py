import requests
from bs4 import BeautifulSoup
from flask import Flask,jsonify

app = Flask(__name__)

def getdataWeb():
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

    listURL = []
    for d in data :
        listURL.append({'logo':'https://theinternship.io/'+d['img']})
    return listURL

@app.route('/companies',methods=['GET'])
def setdate():
    listlogo = getdataWeb()
    objlogo = {
        "companies":listlogo
    }
    return jsonify(objlogo)

@app.route('/',methods=['GET'])
def hello():
    return 'The Internship Thailand 2021 '

if __name__ == "__main__":
    app.run(debug=True)