import requests
from bs4 import BeautifulSoup

date=eval(input("请输入要看的意林期数(格式:年份期数):"))
year=int(date/100)
mouth=date%100
#r = requests.get("http://www.92yilin.com/2015_05/yili20150501.html")
for i in range(1,100):
     if(i<10):
          r = requests.get("http://www.92yilin.com/"+str(year)+"_"+str(mouth)+"/yili"+str(date)+"0"+str(i)+".html")
     else:
          r = requests.get("http://www.92yilin.com/"+str(year)+"_"+str(mouth)+"/yili"+str(date)+str(i)+".html")
     r.encoding = r.apparent_encoding
     html = r.text
        
     soup = BeautifulSoup(html,"html.parser")

     file=open("《意林》"+str(year)+"年第"+str(mouth)+"期.txt","a",encoding='utf-8')
     for i in soup.find_all('p'):
          content=str(i.string)
          file.write(content)
     file.write("\n-------------------------------------------------------------------------------\n")
     file.close()

        



   
