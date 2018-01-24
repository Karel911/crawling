from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from selenium import webdriver


k = 15000496
driver = webdriver.PhantomJS('/Users/mac/Downloads/phantomjs/bin/phantomjs')
url = 'https://www.data.go.kr/dataset/' + str(k) + '/openapi.do'
driver.get(url)
#res = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(driver.page_source, 'lxml')

out = open("api.csv", "w", encoding="utf-8")
out = csv.writer(out)
out.writerow(['id', 'name', 'info', 'dtype', 'api', 'reg_date'])



name = driver.find_element_by_xpath('//*[@id="sub-main"]/div[3]/div/div[2]/div[1]/div/h1/div[1]')#15
#name = driver.find_element_by_xpath('//*[@id="sub-main"]/div[4]/div/div[2]/div[1]/div/h1/div[1]')#30

info = driver.find_element_by_xpath('//*[@id="sub-main"]/div[3]/div/div[2]/div[1]/div/h4')#15
#info = driver.find_element_by_xpath('//*[@id="sub-main"]/div[4]/div/div[2]/div[1]/div/h4')#30

dtype = driver.find_element_by_xpath('//*[@id="sub-main"]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[1]/table/tbody/tr[2]/td[1]')#15
#dtype = driver.find_element_by_xpath('//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[1]')#30

api = driver.find_element_by_xpath('//*[@id="sub-main"]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[1]/table/tbody/tr[2]/td[2]')#15
#api = driver.find_element_by_xpath('//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]')#30

regd = driver.find_element_by_xpath('//*[@id="sub-main"]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[1]/table/tbody/tr[5]/td[1]')#15
#regd = driver.find_element_by_xpath('//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[5]/td[1]')#30


print(name.text.strip())
print(info.text.strip())
print(dtype.text.strip())
print(api.text.strip())
print(regd.text.strip())

out = open("api.csv", "a", encoding="utf-8")
out = csv.writer(out)
out.writerow(dtype.split(" "))