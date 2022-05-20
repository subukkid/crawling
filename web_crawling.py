from urllib import request
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import datetime
import time


df = pd.DataFrame(
    columns=["NO",	"대분류",	"중분류",	"NEIS식품명/상세식품명",	"식품설명",	"포장중량",	"중량단위",	"포장단위"]
)

#print(df.columns)
#print(target_page)
#print(type(target_page))

#print(target_page.select("tbody tr"))
#print(type(target_page.select("tbody tr")))
#print(len(target_page.select("tbody tr")))

for page_number in range(10, 0, -1):
    url = "http://singsing.sejong.go.kr/pages/sub02_01.do?pageIndex=%PAGENUMBER%&tmpcls2=&searchMenu=&searchMenu2=&searchKeyword1="

    original_page = request.urlopen(url.replace("%PAGENUMBER%", str(page_number))).read().decode("utf-8")
    target_page = BeautifulSoup(original_page, "html5lib")


    for tr in reversed(target_page.select("tbody tr")):
        list_td = tr.find_all("td")
        df = df.append({
            "NO": list_td[0].text,
            "대분류": list_td[1].text,
            "중분류": list_td[2].text,
            "NEIS식품명/상세식품명": list_td[3].text,
            "식품설명": list_td[4].text,
            "포장중량": list_td[5].text,
            "중량단위": list_td[6].text,
            "포장단위": list_td[7].text
        }, ignore_index=True)

    time.sleep(2)
 #   print(list_td[0].text)
 #   print(list_td[1].text)
 #   print(list_td[2].text)
 #   print(list_td[3].text)
 #   print(list_td[4].text)
 #   print(list_td[5].text)
 #   print(list_td[6].text)
 #   print(list_td[7].text)
#    print(list_td[0].text, list_td[1].text,list_td[2].text,list_td[3].text,list_td[4].text,list_td[5].text,list_td[6].text,list_td[7].text,sep="|")    
#    df.append([list_td[0].text, list_td[1].text,list_td[2].text,list_td[3].text,list_td[4].text,list_td[5].text,list_td[6].text,list_td[7].text])

#    print(df)
now = datetime.datetime.now()
now_str = now.strftime("%Y%m%d%H%M%S")
df.to_excel("식재료 종류_" + now_str + ".xlsx", index=False)
#    print("----------------------")