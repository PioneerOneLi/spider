#coding=utf-8
import cookielib
import urllib2

#三种获取HTML的方式

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