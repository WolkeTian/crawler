# python 2.7
# 'username' customized, 'password' 0-30
# crawler hurdle 2 'http://www.heibanke.com/lesson/crawler_ex01/'

import urllib
import urllib2

# core code
def getPath(num):
    values = {'username':'wolke', 'password':str(num)}
    data = urllib.urlencode(values)
    url = url = 'http://www.heibanke.com/lesson/crawler_ex01/'
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    result = response.read()
    return result
# core code over

def findValid(tmpNum=15):
    ' 0-30的password中，只有一个是正确的，其他30个返回相同的result. invalidFeedback。找出不同的一个即可'
    if getPath(tmpNum) == getPath(tmpNum+1):
        invalidFeedback = getPath(tmpNum)
        for i in range(31):
            if getPath(i) != invalidFeedback:
                pword = i
                break
    else:  # 则答案在tmpNum 与tmpNum+1之中
        if getPath(tmpNum) == getPath(tmpNum-1):
            pword = tmpNum+1
        else:
            pword = tmpNum        
        
    print ('The correct password is',pword)

if __name__=='__main__':
    findValid()
