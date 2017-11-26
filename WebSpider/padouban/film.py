# coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import sys

class MovieTop250:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.start = 0
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0)'}
        self.movieList = []
        self.filePath = r'C:\Users\B58450\PycharmProjects\untitled\movie.txt'

    def getPage(self):
        URL = 'https://movie.douban.com/top250?start=' + str(self.start)
        request = urllib2.Request(url=URL,headers=self.headers)
        response = urllib2.urlopen(request)
        page = response.read().decode('utf-8')
        pageNum = (self.start + 25)/25
        print '正在抓取第' + str(pageNum) + '页数据...'
        self.start += 25
        return page

    def getMovie(self):
        while self.start <= 225:
            html = self.getPage()
            soup = BeautifulSoup(html,"html.parser")
            for item in soup.find_all('div',class_='item'):
                item_soup = BeautifulSoup(str(item),"html.parser")
                movie = []
                for string in item_soup.stripped_strings:
                    if str(string) != '[可播放]':
                        movie.append(str(string))
                if len(movie) == 8:
                    movie.insert(2,'无')
                self.movieList.append(movie)

        # for movies in self.movieList:
        #     for movie1 in movies:
        #         print movie1
        #     print '*****************'


            # titleList = item_soup.find_all('span', class_='title')
            #
            # if len(titleList) == 2:
            #     name = titleList[0].text+titleList[1].text
            #     # print name
            #     namelist.append(name)
            # else:
            #     namelist.append(titleList[0].text)
        # print title
        #     for item_soup.find_all('p',class_='')


    def writeTxt(self):
        fileTop250 = open(self.filePath,'w')
        for movies in self.movieList:
            for movie in movies:
                # print type(movie)
                # print movie
                fileTop250.write(movie + '\r\n')
            fileTop250.write('***************\r\n')
        print '文件写入成功...'
        fileTop250.close()
#
    def main(self):
        print '正在从豆瓣电影Top250抓取数据...'
        self.getMovie()
        self.writeTxt()
        print '抓取完毕...'
#
DouBanSpider = MovieTop250()
DouBanSpider.main()
