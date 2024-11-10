import requests
from bs4 import BeautifulSoup 
e= requests.get("https://scweb.cwa.gov.tw/zh-tw/earthquake/data/")
soup = BeautifulSoup(e.text,"html.parser")
print(e.text)
sel = soup.select("tr.btnInfo a")
for s in sel:
    print(s["title"], s.text) 