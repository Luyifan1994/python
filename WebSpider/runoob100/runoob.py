# coding:utf-8
# 爬取菜鸟教程python经典100题

from bs4 import BeautifulSoup
from download import load
import time

for i in range(100):
    snum = str(i+1)
    RunoobURL = 'http://www.runoob.com/python/python-exercise-example' + snum + '.html'
    html = load(RunoobURL)
    time.sleep(1)
    soup = BeautifulSoup(html,'lxml')
    title = soup.find(id='content').find_all('p')[1].text
    analysis = soup.find(id='content').find_all('p')[2].text
    content = snum + '. ' + title.replace('\r\n', '') + '\n' + analysis.replace('\r\n', '') + '\n\n\n'
    # print content
    try:
        answer = snum + '. ' + soup.find(class_='hl-main').text + '\n\n'
    except AttributeError:
        answer = snum + '. ' + soup.find_all('pre')[0].text + '\n\n'
        # print answer
    with open('runoob100.txt','a') as f:
        f.write(content)
    with open('runoob_code.txt','a') as p:
        p.write(answer)
        p.write('*************************************************\n')
print 'Done!!!'




