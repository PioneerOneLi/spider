#coding=utf-8
import cookielib
import urllib2
from bs4  import BeautifulSoup
#三种获取HTML的方式

################ urllib2 测试


print "第一种"
url="http://www.zhihu.com"
res=urllib2.urlopen(url)
print res.getcode()
print  len(res.read())


print "第二种"
res =urllib2.Request(url)
res.add_header("User-Agent"," Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36")
res2=urllib2.urlopen(res)
print res2.getcode()
print len(res2.read())


print "第三种"
cj=cookielib.CookieJar()
oper=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(oper)
res3=urllib2.urlopen(url)
print res3.getcode()
print cj
print len(res3.read())


#######################################    我是华丽的分割线 #########################################


##################     BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc)
print soup.prettify()#格式化输出
print soup.p#按照<p>标签输出
print soup.a['class']#输出标签属性为href的内容
print soup.find_all('a')#查找出所有标签为'a'
print soup.find(id="link1")#查询属性id="link1"

for link in soup.find_all('a'):
    print link['href']

print soup.get_text()

count =0
pathName="E:\\2333\\"+str(count+1)+".jpg"
print pathName
