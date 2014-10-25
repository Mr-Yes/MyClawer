#coding=utf-8
import urllib
import re
import socket  
import time  
timeout = 10   
socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置  
sleep_download_time = 2

f = open("E://tianyaUserInfo.txt","a")

#time.sleep(3600)

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
        #print url + '   I am still working'
        for timelist in timeList:
            print>>f, timelist
    page.close()

for id in range(164107,200000):
    idURL = 'http://www.tianya.cn/'+ '%s' %id
    try:
        getTime(idURL)
    except IOError,e:
        if e.message == "timed out":
            id = id - 1;
            print 'Warning: Timeout'
    #time.sleep(sleep_download_time)

f.close()
    


    
