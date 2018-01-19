from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd


out = open("exapp.csv", "w", encoding="utf-8")
out = csv.writer(out)
out.writerow(['id', 'name', 'url', 'info', 'purpose', 'exinfo_date', 'exinfo_os', 'exinfo_dev',
            'exinfo_loc', 'exinfo_corp', 'exinfo_regd'])

#start 495   #4999 10000 empty
for k in range(1008603,1008774):
    url = 'https://www.data.go.kr/useCase/' + str(k) + '/exam.do'
    res = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(res, 'lxml')

    sort = soup.find_all('dt')

    for c in sort:
        if(c.string == "분류 : 문화관광"):
            out = open("exapp.csv", "a", encoding="utf-8")
            out = csv.writer(out)
            name = soup.find_all('p', class_='title')
            category = soup.find_all('dt')
            url = soup.find_all('dd')
            info = soup.find_all('p')
            info = info[2]
            purpose = soup.find_all('div', class_='utxt')

            exinfo = soup.find_all('td')
            exinfo_date = exinfo[0]
            exinfo_os = exinfo[1]
            exinfo_dev = exinfo[2]
            exinfo_loc = exinfo[3]
            exinfo_corp = exinfo[4]
            exinfo_regd = exinfo[5]


            for n, u, p, date, os, dev, loc, regd in zip(name, url, purpose, exinfo_date, exinfo_os,
                                                                 exinfo_dev, exinfo_loc, exinfo_regd):
                id = k
                n = n.string
                u = u.a.string
                i = info.text.strip()
                p = p.text
                date = date.string
                os = os.string.strip()
                dev = dev.string
                loc = loc.string
                corp = exinfo_corp.text
                regd = regd.string


                out.writerow([id, n, u, i, p, date, os, dev, loc, corp, regd])
                print(url)


        else:
            print("=============")


