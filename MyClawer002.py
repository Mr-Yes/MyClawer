#coding=utf-8
import urllib
import re
import socket  
import time  
timeout = 10   
socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置  
sleep_download_time = 2

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        time.sleep(sleep_download_time)
        x+=1

#html = getHtml("http://www.japaneseslurp.com")
html = getHtml("http://bookoferotica.com/")
print getImg(html),'Well Done'
