import requests
from bs4 import BeautifulSoup
import bs4
#import lxml
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30,headers={'user-agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ilist, html):
    xlist=[]
    soup = BeautifulSoup(html, "xml")
    for it in soup.find('channel').children:
        if isinstance(it, bs4.element.Tag):
            if it.name=='item':
                itc=it.contents
                itd=itc[-1].contents[0] #description
                itds=itd.string
                soup1=BeautifulSoup(itds,"xml")
                for itn in soup1.find('div').children:
                    
                    if itn.name=='br' or 'strong':
                        if isinstance(itn,bs4.element.NavigableString):
                            xlist.append(itn.string)
                        elif itn.name=='strong':
                            xlist.append(itn.string)
                ilist.append(xlist)
                xlist=[]

def printUnivList(ilist):
    print("资源个数："+str(len(ilist))+"\n\n")
    #print(ilist)
    for i in ilist:
        #print(type(u[0]))
        print("{:^10}\t{:^10}\t{:^10}\t{:^10}\n\n".format(i[1],i[2],i[3],i[5]))

def main():
    info = []
    url = 'https://msdn.itellyou.cn/rss.ashx'
    html = getHTMLText(url)
    fillUnivList(info, html)
    printUnivList(info)

main()
