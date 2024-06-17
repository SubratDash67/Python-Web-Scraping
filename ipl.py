import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_="ih-td-tab auction-tbl")
title = table.find_all("th")
# print(title)
# print(table)
headers = []
for i in title:
    name = i.text
    headers.append(name)

print(headers)
df = pd.DataFrame(columns=headers)
rows = table.find_all("tr")
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row

print(df)
df.to_csv("ipl.csv")
