from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from selenium import webdriver
import pandas as pd

target = pd.read_csv('~/downloads/apiurl.csv')
driver = webdriver.PhantomJS('/Users/mac/Downloads/phantomjs/bin/phantomjs')

out = open("api.csv", "w", encoding="utf-8")
out = csv.writer(out)
out.writerow(['id', 'name', 'info', 'dtype', 'api', 'reg_date'])


for i in target['url']:
    url = 'https://www.data.go.kr/dataset/' + str(i) + '/openapi.do'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    name3 = driver.find_element_by_xpath('//*[@id="sub-main"]/div[3]/div/div[2]/div[1]/div/h1/div[1]')
    name4 = driver.find_element_by_xpath('//*[@id="sub-main"]/div[4]/div/div[2]/div[1]/div/h1/div[1]')
    if(name3 == None):
        out = open("test.csv", "a", encoding="utf-8")
        out = csv.writer(out)
        n = name3.string
        out.writerow([i, n])#, sup, ser, info])
        print("N3")
    elif(name3 != None):
        out = open("test.csv", "a", encoding="utf-8")
        out = csv.writer(out)
        n = name4.string
        out.writerow([i, n])  # , sup, ser, info])
        print("N4")


