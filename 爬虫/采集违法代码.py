#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
from cache import CacheTool
import time

url = "http://jiaojing.chegonggong.com/illegalcode/querybycode/?code=&ga=gh_a68f124f7fbf"

csv_file = open("./违法代码.csv","a")
csv_writer = csv.writer(csv_file)

try:
    #gbk编码打开
    with open('./xx.csv',"r",encoding="gbk") as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            
            flag = CacheTool.sadd(row[1])

            if not flag:
                continue
            
            print(row[0]+'-'+row[1])

            payload = {"illegalCode" : row[1]}
            time.sleep(1)
            respone = requests.post(url,data = payload)
            print(respone)
            res = respone.content.decode('utf-8')         

            html = BeautifulSoup(res,'lxml')

            div = html.select('.info')

            if not div:
                continue
                
            ddEle = html.select('.base dd')
        
            info = []
            for item in ddEle:
                info.append(item.text.strip())

            detail =  "依据"+info[0]+' 和 '+info[1]+',记'+info[2]+'分,'+'罚款'+info[3]+'元,'+info[4]
            if info[5] != '无':
                detail = detail + ','+info[5]
            
            arr = [row[1]] + [row[2]] + [detail]

            csv_writer.writerow(arr)

    print('ok')

except Exception as e:
        print(e)

