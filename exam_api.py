from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd

target = pd.read_csv('~/downloads/exam.csv')

out = open("test.csv", "w", encoding="utf-8")
out = csv.writer(out)
out.writerow(['id', 'name', 'api_sup', 'api_service', 'api_info'])




for i in target['id']:
    url = 'https://www.data.go.kr/useCase/' + str(i) + '/exam.do'
    res = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(res, 'lxml')
    name = soup.find_all('p', class_='title')
    list = soup.find('tbody', class_="list")
    if(list == None):
        for n in name:
            out = open("test.csv", "a", encoding="utf-8")
            out = csv.writer(out)
            n = n.string
            sup = None
            ser = None
            info = None
            out.writerow([i, n, sup, ser, info])
            print("None")
    elif(list != None):
        row = list.find_all('tr')
        for n in name:
            out = open("test.csv", "a", encoding="utf-8")
            out = csv.writer(out)
            n = n.string
            for r in row:
                col = r.find_all('td')
                sup = col[0].string
                ser = col[1].text.strip()
                info = col[2].text.strip()
                out.writerow([i, n, sup, ser, info])
                print(i)