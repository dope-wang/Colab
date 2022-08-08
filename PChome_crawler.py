import requests
import io
import prettytable
import json
import codecs
produc_name=input("關鍵字 ：")
r1=requests.get(
      "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
      headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "cookie":"ECC=b7b9bf8c30c8acada2c8128b0c89fee9f14fbefb.1651816537; _gcl_au=1.1.946280473.1651816541; venguid=79b017d4-372d-41a5-a3a2-2170048f7a0f.wgc-ngxx20220506; FPID=FPID2.3.t29oMEb5v6pdMxJTn2j2RWkcQRviyYg61BRdaO4PhVQ%3D.1651816541; U=56c40c26808213f1c210ddeda0e50e0f79c7c22f; ECWEBSESS=730046f894.2229ed47b3671ee8be58cdb4b1dec01af477fcec.1651816612; _gid=GA1.3.457126016.1652340390; FPLC=oaynubXq25KQKEtCmbQmHROPiC5f7Kz3DbZ0bzFCTN6N7sTh6JB4PML1fb7qcQHqo0QQakgxSu3Zo2ORIgtErcWOcZx6dORjDsXf%2Fj7xcWgf5hGJS2wKgiWW2oNdGw%3D%3D; _ga_9876543211=GS1.1.1652342927.3.0.1652342927.0; gsite=shopping; vensession=28663214-b2c8-438b-9944-8a812a77aa7a.wgc-5csj20220513.se; _ga_9CE1X6J1FG=GS1.1.1652408430.5.1.1652408451.39; _ga_9876543210=GS1.1.1652408430.5.1.1652408451.0; _ga=GA1.3.2146884030.1651816541"
      },
      params={
          "q":produc_name,
          "page":"1",
          "sort":"sale/dc"
      },
      data={}
  )
result=json.loads(r1.text)
p1=prettytable.PrettyTable(["名稱","價格"], encoding="utf-8")
p1.align["名稱"]="l"
for i in result["prods"]:
  p1.add_row([i["name"],i["price"]])

print(p1)

user_input = input("前往頁碼 ：")

r1=requests.get(
      "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
      headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "cookie":"ECC=b7b9bf8c30c8acada2c8128b0c89fee9f14fbefb.1651816537; _gcl_au=1.1.946280473.1651816541; venguid=79b017d4-372d-41a5-a3a2-2170048f7a0f.wgc-ngxx20220506; FPID=FPID2.3.t29oMEb5v6pdMxJTn2j2RWkcQRviyYg61BRdaO4PhVQ%3D.1651816541; U=56c40c26808213f1c210ddeda0e50e0f79c7c22f; ECWEBSESS=730046f894.2229ed47b3671ee8be58cdb4b1dec01af477fcec.1651816612; _gid=GA1.3.457126016.1652340390; FPLC=oaynubXq25KQKEtCmbQmHROPiC5f7Kz3DbZ0bzFCTN6N7sTh6JB4PML1fb7qcQHqo0QQakgxSu3Zo2ORIgtErcWOcZx6dORjDsXf%2Fj7xcWgf5hGJS2wKgiWW2oNdGw%3D%3D; _ga_9876543211=GS1.1.1652342927.3.0.1652342927.0; gsite=shopping; vensession=28663214-b2c8-438b-9944-8a812a77aa7a.wgc-5csj20220513.se; _ga_9CE1X6J1FG=GS1.1.1652408430.5.1.1652408451.39; _ga_9876543210=GS1.1.1652408430.5.1.1652408451.0; _ga=GA1.3.2146884030.1651816541"
      },
      params={
          "q":produc_name,
          "page":user_input,
          "sort":"sale/dc"
      },
      data={}
  )
result=json.loads(r1.text)
p1=prettytable.PrettyTable(["名稱","價格"], encoding="utf-8")
p1.align["名稱"]="l"
for i in result["prods"]:
  p1.add_row([i["name"],i["price"]])

print(p1)
    