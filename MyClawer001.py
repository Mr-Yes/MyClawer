import urllib
import re

def getHtml(url):
    html= urllib.urlopen(url)
    page = html.read()
    print(page)

url = 'www.baidu.com'
getHtml(url)

'''
def callbackfunc(blocknum, blocksize, totalsize):

    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent

url = 'http://www.bdwm.net'
local = 'e:\\pku.html'
urllib.urlretrieve(url, local, callbackfunc)
'''
