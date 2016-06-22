# http://www.heibanke.com/lesson/crawler_ex00/ The first crawler hurdle.

baseUrl = 'http://www.heibanke.com/lesson/crawler_ex00/'
import re
import urllib.request as urlmod
def getNum(url):
    page = urlmod.urlopen(url)
    html = str(page.read())
    reg = r'\\x\w{2}(\d{5}).*</h3>\\n'
    reg = re.compile(reg)
    num = reg.findall(html)
    return num
url = baseUrl
times = 0
while True:
    num = getNum(url)
    try:
        url = baseUrl+num[0]
        print ('running',times,'times')
        times += 1
        print (url)
    except IndexError:
        print ('Done',',the right answer is',url)
        break
