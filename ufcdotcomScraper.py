import csv
from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.ufc.com/fighter/Weight_Class/filterFighters?offset=%s&max=20&sort=lastName&order=asc&weightClass=&fighterFilter=Current'

def get_ufc_data(url):
    maxoffset= 780
    with open('ufcfighters.csv', 'w') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow(["Name","Record","Height","Weight"])
        for offset in range(0, maxoffset+1, 20):
            page = url % offset
            r = requests.get(page)
            html = BeautifulSoup(r.text, 'html.parser')
            fighters = list(html.find_all("tr", class_="fighter"))
            for fighter in fighters:
                try:
                    name = fighter.find('a', class_='fighter-name').text.strip()
                    record = fighter.findAll('div', class_='main-txt')[0].text.strip()
                    height = fighter.findAll('div', class_='sub-txt')[1].text.strip()
                    weight = fighter.findAll('div', class_='main-txt')[2].text.strip()
                    writer.writerow([name,record.replace('"',''),re.sub("[^0-9]", "", height),re.sub("[^0-9]", "",weight)])
                except:
                    print("error at: "+str(name)+"\n")
                    
get_ufc_data(url)