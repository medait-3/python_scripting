import requests
import urllib.request

#Read url as one big string
def readUrlContnet():
    link = "https://www.google.dk/"
    f = requests.get(link)
    print(f.text)

#save url content to file
def saveUrlContent():
    myurl = 'https://www.google.dk/'
    myreq = urllib.request.urlopen(myurl)
    mydata = myreq.read()
    with open('mydata.html', 'wb') as ofile:
        ofile.write(mydata)

#Crawl multiple pages
def crawlPage():
    for i in range(1451720, 1451730):
        link = "https://www.mmo-champion.com/members/" + str(i)
        f = requests.get(link)
        print(f.text)

crawlPage()