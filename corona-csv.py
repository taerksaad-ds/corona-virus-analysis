from urllib.request import Request, urlopen as urReq
from bs4 import BeautifulSoup as soup
import datetime
def scrapCertainUrl(url):
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = urReq(r)
    page_html = uClient.read()
    uClient.close ()
    return soup(page_html, "html5lib")

def checkRow(row):
    if row != None: 
        row = row.text.replace(',','').replace('+','') 
    else: 
        row = "None" 
    return row
f = open("coronavirus2.csv" , "w")
f.write ("date, country, totalcases, newcases, totaldeath, newdeath, totalrecovered, activecases, seriouscases, totaltests\n")    

page_soup = scrapCertainUrl('https://www.worldometers.info/coronavirus/')
table = page_soup.find("table", {"id":"main_table_countries_yesterday"}).tbody
reports = table.findAll ("tr")
counter = 0

for report in reports:
    if counter < 8:
        counter += 1
        continue
    date= str(datetime.datetime.today()).split()[0]

    tds = report.findAll("td")
    country= tds[0].text
    totalcases= tds[1].text.replace(',', '')
    newcases = tds[2]
    totaldeath= tds[3]
    newdeath = tds[4]
    totalrecovered= tds[5].text.replace(',','')
    activecases= tds[6].text.replace(',','')
    seriouscases= tds[7].text.replace(',','')
    totaltests= tds[10].text.replace (',','')
    
    newcases = checkRow(newcases)
    totaldeath = checkRow(totaldeath)
    newdeath = checkRow(newdeath)
       
    
    f.write (date + ","+country+ ","+totalcases+ ","+newcases+ ","+ totaldeath+ ","+ newdeath + "," + totalrecovered + "," + activecases + "," + seriouscases + "," + totaltests + "\n")
    

        


    #totalcases = int(totalcases)
    # newcases = int(newcases)
    counter += 1


f.close()