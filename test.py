#coding=utf-8
import urllib
import re
import socket  
import time  
timeout = 10   
socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置  
sleep_download_time = 2

f = open("E://tianyaUserInfo.txt","w")

def getTime(url):
    page = urllib.urlopen(url)
    html = page.read()    
    print>>f, ''
    userRE = re.compile(r'uname="(.+?)" uid="(.+?)"')
    userInfo = re.findall(userRE,html)
    if userInfo is not None:
        for info in userInfo:
            print>>f, info
    timeRE = re.compile(r'<p>(.+?)</p>')
    timeList = re.findall(timeRE,html)
    if timeList is not None:
        print 'I am still working'
        for timelist in timeList:
            print>>f, timelist
    page.close()

for id in range(100000,100100):
    print id
    idURL = 'http://www.tianya.cn/'+ '%s' %id
    getTime(idURL)
    time.sleep(sleep_download_time)

f.close()
    


    
