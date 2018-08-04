import csv
from bs4 import BeautifulSoup
import requests
import re
import string

url = "http://www.fightmetric.com/statistics/fighters?char="

def getUFCdata(url):
    with open('fightmetricclean.csv', 'w') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow(["First", "Last", "Nickname", "Ht", "Wt", "Reach", "Stance", "Win", "Loss", "Draw", "Belt"])
        for char in string.ascii_lowercase:
            r = requests.get(url+char+"&page=all")
            print(url+char+"&page=all")
            html = BeautifulSoup(r.text, 'html.parser')
            fighters = list(html.find_all("tr", class_="b-statistics__table-row"))
            for fighter in fighters:
                row = list(fighter.find_all("td", class_="b-statistics__table-col"))
                try:
                    writer.writerow([ x.get_text().strip() for x in row])
                except:
                    print("missing data")
getUFCdata(url)