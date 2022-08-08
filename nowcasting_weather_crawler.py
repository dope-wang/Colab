import requests
import io
import prettytable
import codecs
from bs4 import BeautifulSoup
import json

r1=requests.get(
      "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
      headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "referer":"https://www.cwb.gov.tw/V8/C/W/County_TempTop.html",
        "cookie":"_ga=GA1.3.1521902014.1652428386; _gid=GA1.3.223488433.1652428387; TS558d33eb027=08dc4bbcbbab20007d52365be573a39994b2b5d3206bb06d6043b1926a26138791437e47ff8d68ab08c8ac7327113000b237fa2704f45d730b2e2f02f24bd82c3781728019d6de2a8e8a7dd542ae5a57b8c6baaa29c22492349d5fe36f9271bd; TS010c55bd=0107dddfef717e5b845490678ec39dc8732249d3d3feb8a87aece8d7db6de3ce8fa7ca1612cfd979e73066f9239127187cc6993cad; _ga_K6HENP0XVS=GS1.1.1652428386.1.1.1652429785.0"
      },
  )


p1=BeautifulSoup(r1.text, "html.parser")

 

result=p1.find_all("th", {
  "scope":"row"
})
p1=prettytable.PrettyTable(["地區","氣溫"], encoding="utf-8")
for i in result:
  p1.add_row([i.text,i.parent.find("span",{"class":"tem-C is-active"}).text])
print(p1)