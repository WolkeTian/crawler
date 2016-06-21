import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html=str(page.read())   # page.read() outputs byte format
    return html

def getImgLinks(html):

    reg = r'src="(http://.{,250}\.jpg)"'
    imgre = re.compile(reg)
    imgLinkList=imgre.findall(html)
    return imgLinkList

def downloadImg(imgLinkList):
    mark=0
    print ('Downloading....')
    for link in imgLinkList:
        fileName = 'py3ImgCrawler%s%i.jpg'%(link[-7:-4],mark)
        urllib.request.urlretrieve(link,fileName)
        print ('%s downloaded' % fileName)
        mark+=1

def runCrawler():
    url = input('Enter the url you want to crawl img from')
    html = getHtml(url)
    imgLinkList = getImgLinks(html)
    print (imgLinkList)
    downloadImg(imgLinkList)

if __name__=='__main__':
    runCrawler()
    print ('All done')
